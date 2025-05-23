import logging, json, asyncio

from collections.abc import Callable, Coroutine
import attr

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback

from homeassistant.components.input_number import (
    ATTR_VALUE as INP_ATTR_VALUE,
    DOMAIN as NUMBER_DOMAIN,
    SERVICE_RELOAD as NUMBER_SERVICE_RELOAD,
    SERVICE_SET_VALUE as NUMBER_SERVICE_SET_VALUE,
)
from homeassistant.components.input_select import (
    DOMAIN as SELECT_DOMAIN,
    SERVICE_RELOAD as SELECT_SERVICE_RELOAD,
    SERVICE_SELECT_OPTION as SELECT_SERVICE_SET_OPTION,
)
from homeassistant.components.input_boolean import (
    DOMAIN as BOOLEAN_DOMAIN,
    SERVICE_RELOAD as BOOLEAN_SERVICE_RELOAD,
)

from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_OPTION,
)
from homeassistant.core import HomeAssistant
from homeassistant.components import mqtt


from .const import (
    DOMAIN,
    CONF_ID,
    CONF_MQTT_NODE,
    CONF_MQTT_DBG,
    CONF_LANGUAGE,
    CONF_FREQ,
    AVAILABLE_LANGUAGES,
)

# import Remko register defines
from .remko_regs import (
    FIELD_MAXVALUE,
    FIELD_MINVALUE,
    FIELD_REGNUM,
    FIELD_REGTYPE,
    FIELD_UNIT,
    id_names,
    reg_id,
    query_list,
)

_LOGGER = logging.getLogger(__name__)


class HeatPump:
    _dbg = True
    _mqtt_base = ""
    _langid = 0
    unsubscribe_callback: Callable[[], None]

    # ###
    @callback
    async def message_received(self, message):
        """Handle new MQTT messages."""
        _LOGGER.debug("%s: message.payload:[%s]", self._id, message.payload)
        try:
            json_dict = json.loads(message.payload)
            json_dict = json_dict.get("values")
            if message.topic == self._data_topic:
                for k in json_dict:
                    # Map incomming registers to named settings based on id_reg (Remko_regs)
                    if k in self._id_reg and json_dict[k] != "":
                        _LOGGER.debug("id [%s] value [%s] => [%s]", k, self._hpstate[k], json_dict[k])
                        # Internal mapping of Remko_MQTT regs, used to create update events
                        temp = self._hpstate[k]
                        self._hpstate[k] = json_dict[k]
                        if reg_id[self._id_reg[k]][1] == "switch":
                            self._hpstate[k] = int(self._hpstate[k], 16) > 0
                        if reg_id[self._id_reg[k]][1] == "sensor_el":
                            self._hpstate[k] = int(self._hpstate[k], 16) * 100
                        if reg_id[self._id_reg[k]][1] == "sensor_elc":
                            # this field type is 1/100th of Watt, ridiculous and gets lots
                            # of updates, limit accepted changes, to avoid too many 
                            # database updates.
                            new = int(self._hpstate[k], 16)
                            new = int(new / 100)
                            old = int(temp)
                            if new - old > 1:
                                new = new - 1
                            elif new - old < -1:
                                new = new + 1
                            else: 
                                new = old
                            self._hpstate[k] = new
                        if reg_id[self._id_reg[k]][1] == "sensor_en":
                            # dont know how to translate, but it is definately not plain kWh
                            self._hpstate[k] = int(self._hpstate[k], 16)
                        if reg_id[self._id_reg[k]][1] == "number":
                            self._hpstate[k] = int(self._hpstate[k], 16)
                        if reg_id[self._id_reg[k]][1] in [
                            "temperature",
                            "temperature_input",
                        ]:
                            try:
                                # deal with negative numbers
                                new = int(self._hpstate[k], 16)
                                if new > 32768:
                                    new = new - 65536
                                # smooth temperature to avoid too many database updates 
                                # temperature will always be 0.2 "behind"
                                if reg_id[self._id_reg[k]][1] == "temperature":
                                    old = int(temp * 10)
                                    if new - old > 2:
                                        new = new - 2
                                    elif new - old < -2:
                                        new = new + 2
                                    else: 
                                        new = old
                                # store new (or old value) in float     
                                self._hpstate[k] = new / 10
                            except:
                                _LOGGER.error("FAIL id [%s] value [%s] => [%s]", k, temp, json_dict[k])
                                try:
                                    new = int(self._hpstate[k], 16)
                                    if new > 32768:
                                        new = new - 65536
                                    self._hpstate[k] = new / 10
                                except:
                                    # sometimes an empty result is received: "1946": ""
                                    # should be catched in top, will add code, but also except handling
                                    # here. Restore old value
                                    self._hpstate[k] = temp
                        if reg_id[self._id_reg[k]][1] == "sensor_mode":
                            mode = f"opmode{int(json_dict[k], 16)}"
                            self._hpstate[k] = id_names[mode][self._langid]
                        if reg_id[self._id_reg[k]][1] == "select_input":
                            if self._id_reg[k] == "main_mode":
                                mode = f"mode{int(json_dict[k], 16)}"
                            elif self._id_reg[k] == "dhw_opmode":
                                mode = f"dhwopmode{int(json_dict[k], 16)}"
                            self._hpstate[k] = id_names[mode][self._langid]
                    else:
                        _LOGGER.debug("IGNORE [%s] [%s]", k, json_dict[k])
                self._hpstate["communication_status"] = json_dict.get(
                    "vp_read", "Ok"
                )

                self._hass.bus.fire(
                    self._domain + "_" + self._id + "_msg_rec_event", {}
                )
            else:
                _LOGGER.error("JSON result was not from Remko-mqtt")
        except ValueError:
            _LOGGER.debug("MQTT payload could not be parsed as JSON")
            _LOGGER.error("Erroneous JSON: %s", message.payload)

        if self._mqtt_counter == 1:
            self._mqtt_counter = 0
            await self.mqtt_keep_alive()

    def __init__(self, hass, entry: ConfigEntry):
        self._hass = hass
        self._entry = entry
        self._hpstate = {}
        self._domain = DOMAIN
        self._id = entry.data[CONF_ID]
        self._id_reg = {}
        self.unsubscribe_callback = None
        self._freq = entry.data[CONF_FREQ]
        #self._mqtt_counter = entry.data[CONF_FREQ]

        # Create reverse lookup dictionary (id_reg->reg_number)

        for k, v in reg_id.items():
            self._id_reg[v[0]] = k
            self._hpstate[v[0]] = -1

    async def setup_mqtt(self):
        self.unsubscribe_callback = await mqtt.async_subscribe(
            self._hass,
            self._data_topic,
            self.message_received,
        )
        # """ Wait before getting new values """
        #await asyncio.sleep(5)
        #self._mqtt_counter = self._freq
        self._mqtt_counter = 1
        await self.mqtt_keep_alive()
        self._hass.bus.fire(self._domain + "_" + self._id + "_msg_rec_event", {})

    async def remove_mqtt(self):
        self.unsubscribe_callback = await mqtt.async_unload_entry(
            self._hass,
            self._data_topic,
            self.message_received,
        )

    async def update_config(self, entry):
        if self.unsubscribe_callback is not None:
            self.unsubscribe_callback()
        lang = entry.data[CONF_LANGUAGE]
        self._langid = AVAILABLE_LANGUAGES.index(lang)
        self._dbg = entry.data[CONF_MQTT_DBG]
        self._mqtt_base = entry.data[CONF_MQTT_NODE] + "/SMTID/"
        self._data_topic = self._mqtt_base + "HOST2CLIENT"
        self._cmd_topic = self._mqtt_base + "CLIENT2HOST"
        self._freq = entry.data[CONF_FREQ]

        # Provide some debug info
        _LOGGER.debug(
            f"INFO: {self._domain}_{self._id} mqtt_node: [{entry.data[CONF_MQTT_NODE]}]"
        )

        if self._dbg is True:
            self._mqtt_base = self._mqtt_base + "dbg_"
            _LOGGER.error("INFO: MQTT Debug write enabled")

        _LOGGER.debug("Language[%s]", self._langid)

        await self.mqtt_keep_alive()

    async def async_reset(self):
        """Reset this heatpump to default state."""
        # unsubscribe here
        return True

    @property
    def hpstate(self):
        return self._hpstate

    def get_value(self, item):
        """Get value for sensor."""
        res = self._hpstate.get(item)
        _LOGGER.debug("get_value(" + item + ")=%d", res)
        return res

    def update_state(self, command, state_command):
        """Send MQTT message to Remko."""
        _LOGGER.debug("update_state:" + command + " " + state_command)

    # ### ##################################################################
    # Write specific value_id with data, value_id will be translated to register number.
    # Default service used by input_number automations

    async def send_mqtt_reg(self, register_id, value) -> None:
        """Service to send a message."""

        register = reg_id[register_id][0]
        _LOGGER.debug("register:[%s]", register)

        if not (isinstance(value, int) or isinstance(value, float)) or value is None:
            _LOGGER.error("No MQTT message sent due to missing value:[%s]", value)
            return

        if not (register in self._id_reg):
            _LOGGER.error("No MQTT message sent due to unknown register:[%s]", register)
            return

        reg_type = reg_id[register_id][1]
        if reg_type == "temperature_input":
            topic = self._cmd_topic
            if (value < 0):
                hex_str = hex(int((value * 10) + 65536)).upper()
            else:
                hex_str = hex(int(value * 10)).upper()
            hex_str = hex_str[2:].zfill(4)
            payload = json.dumps({"values": {register: hex_str}})
        elif register_id in [
            "dhw_opmode",
            "main_mode",
        ]:
            topic = self._cmd_topic
            if register_id == "main_mode":
                value = value + 1
            value = str(value).zfill(2)
            payload = json.dumps({"values": {register: value}})
        elif register_id in [
            "absence_mode",
            "party_mode",
        ]:
            topic = self._cmd_topic
            hex_str = hex(int(value))
            hex_str = hex_str[2:].zfill(2)
            payload = json.dumps({"values": {register: hex_str}})

        _LOGGER.debug("topic:[%s]", topic)
        _LOGGER.debug("payload:[%s]", payload)
        self._hass.async_create_task(
            mqtt.async_publish(self._hass, topic, payload, qos=2, retain=False)
        )
        """ Wait before getting new values """
        #await asyncio.sleep(5)
        #self._mqtt_counter = self._freq
        #self._hass.bus.fire(self._domain + "_" + self._id + "_msg_rec_event", {})

    async def mqtt_keep_alive(self) -> None:
        """Heatpump sends MQTT messages only when triggered."""

        topic = self._cmd_topic
        if query_list:
            payload = json.dumps({"FORCE_RESPONSE": True, "query_list": query_list})
        else:
            payload = json.dumps({"FORCE_RESPONSE": True})

        #max. frequency in which a request is posted is 30 seconds. 
        self._mqtt_counter = 0
        await asyncio.sleep(30)
        self._mqtt_counter = 1
        
        _LOGGER.debug("topic:[%s]", topic)
        _LOGGER.debug("payload:[%s]", payload)

        self._hass.async_create_task(
            mqtt.async_publish(self._hass, topic, payload, qos=2, retain=False)
        )
