"""Constants for the component."""

# Component domain, used to store component data in hass data.
DOMAIN = "remko_mqtt"

# == Remko Const
CONF_ID = "id_name"
CONF_NAME = "Remko MQTT"
CONF_VER = "v0.8.3"
CONF_MQTT_NODE = "V04P28"
CONF_MQTT_DBG = "remko_dbg"
CONF_LANGUAGE = "language"
CONF_DATA = "data_msg"
CONF_FREQ = "freq"
DEFAULT_DBG = False

# Internal "no data received yet" value in _hpstate, never published as a
# sensor state: entities map it to None so they show unknown until the first
# real MQTT message arrives.
INITIAL_STATE = -1
AVAILABLE_LANGUAGES = ["de", "en", "fr", "it", "nl"]


PLATFORM_AUTOMATION = "automation"
PLATFORM_GROUP = "group"
CONF_ENTITY_PLATFORM = "entity_platform"
