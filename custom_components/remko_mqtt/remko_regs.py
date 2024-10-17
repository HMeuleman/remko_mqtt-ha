# Remko generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4

# Query list
#query_list = []
query_list = [127, 132, 327, 1014, 1088, 1893, 1894, 1946, 1951, 5001, 5032, 5036, 5123, 5039, 5190, 5320, 5693, 5822, 5824]
client_id = "xxx"

# Register as sensors
reg_id = {
    #  reg_id: ['reg#', 'type', 'unit', 'min', 'max'],
    "language": ["1014", "string", "", "", ""],
    "version": ["327", "number", "", "" , "" ],
    "user_level": ["5029", "string", "", "", ""],
    #"dhw_opmode": ["1079", "select_input", "", 0, 16],
    #"water_temp_req": ["1082", "temperature_input", "ÂºC", 20.0, 60.0],
    "temp_req": ["1946", "temperature_input", "ÂºC", -10.0, 10.0],
    "absence_mode": ["1893", "switch", "", "", ""],
    "party_mode": ["1894", "switch", "", "", ""],
    "main_mode": ["1088", "select_input", "", "", ""],
    "opmode": ["5001", "sensor_mode", "", "", ""],
    "out_temp": ["5032", "temperature", "ÂºC", 0, 40],
    "floor_temp": ["5036", "temperature", "ÂºC", 0, 70],
    "return_floor_temp": ["5123", "temperature", "ÂºC", 0, 70],
    "verw_water_temp": ["5190", "temperature", "ÂºC", 0, 70],
    "el_consumption": ["5320", "sensor_el", "W", 0, 6000],
    "dhw_heating": ["5693", "action", "", "", ""],
    "comp_starts": ["5822", "number", "", "" , "" ],
    "comp_hours": ["5824", "number", "", "" , "" ],
    "communication_status": ["communication_status", "generated_sensor", "", 0, 0],
}

# Translation dictionary
#  'de', 'en', 'fr', 'it', 'nl']
id_names = {
    "language": ["Sprache", "Language", "Langue", "Lingua", "Taal"],
    "version": ["Version number", "Versionsnummer", "Versionsnummer", "Versionsnummer", "Versionsnummer"],
    "user_level": ["user level", "user level", "user level", "user level", "user level"],
    #"water_temp_req": ["Water temp. req.", "Warmwasser soll", "Warmwasser soll", "Warmwasser soll", "Warmwasser soll"],
    "temp_req": ["KÃ¤lter / WÃ¤rmer", "Colder / hotter", "Plus froid / Plus chaud", "PiÃ¹ freddo / piÃ¹ caldo", "Kouder / Warmer"],
    "out_temp": ["AuÃŸentemperatur", "Outside temperature", "TempÃ©rature extÃ©rieure", "Temp. esterna", "Buitentemperatuur"],
    "floor_temp": ["Ist-Temperatur", "Actual temperature", "TempÃ©rature rÃ©elle", "Temp. Circ.", "Vloerverwarming temp."],
    "return_floor_temp": ["RÃ¼cklauftemp", "Return temp.", "Temp. retour", "Temp. ritorno", "Vloerverwarming retour temp."],
    "verw_water_temp": ["Heizwasser Ist-Temp.", "Heating water temp. (actual)", "Temp. eau chaude (Val.r rÃ©elle)", "Temp. Produzione", "Verw. watertemp (act. waarde)"],
    "el_consumption": ["Leistung elektrisch", "electr. power heatpump", "Puissance Ã©lectr. thermopompe", "Ass. elettrico PDC", "Elektr. Vermogen warmtepomp"],
    "main_mode": ["Raumklima Modus", "Room climate mode", "Mode de climat ambiant", "ModalitÃ  Clima ambiente", "Ruimteklimaat-Modus"],
    "opmode": ["Aktuelle Betriebsart", "Current operating mode", "Mode de fonctionnement actuel", "Modo operativo attuale", "Actuele bedrijfstoestand"],
    #"dhw_opmode": ["Modus", "Mode", "Mode", "Modo funzionamento", "Modus"],
    "absence_mode": ["Abwesenheitsmodus", "Absence mode", "Mode d'absence", "ModalitÃ  Assenza", "Afwezig mode"],
    "party_mode": ["Partymodus", "Party mode", "Mode de fÃªte", "ModalitÃ  Party", "Partymodus"],
    "dhw_heating": ["1x WW aufheizen", "1x DHW heating", "1x WW Chauffage", "Riscaldare 1 x AC", "1x WW Opwarmen"],
    "comp_starts": ["Kompressorstarts", "Compressor starts", "DÃ©marrages de compresseurs", "Avviamenti compressore", "Compressor opstarts"],
    "comp_hours": ["Laufzeit (Stunden)", "Runtime (hours)", "DurÃ©e (heures)", "Ore funzionamento", "Looptijd (uren)"],
    "mode1": ["Auto", "Auto", "Auto", "Auto", "Auto"],
    "mode2": ["Heizen", "Heating", "Chauffage", "Riscald.", "Verwarmen"],
    "mode3": ["Standby", "Standby", "Standby", "Standby", "Standby"],
    "mode4": ["KÃ¼hlen", "Cooling", "Refroidissement", "Raffredd.", "Koelen"],
    "dhwopmode0": ["Automatik Komfort", "Automatic comfort", "Automatic comfort", "Automatic comfort", "Automatisch comfort"],
    "dhwopmode1": ["Automatik Eco", "Automatic eco", "Automatic eco", "Automatic eco", "Automatisch eco"],
    "dhwopmode2": ["Nur Solar/PV", "Solar/PV only", "Solar/PV only", "Solar/PV only", "Zonnepanelen enkel", ],
    "dhwopmode3": ["Aus", "Off", "Off", "Off", "Uit"],
    "opmode1": ["StÃ¶rung", "Forced off", "Forced off", "Forced off", "Forced off"],
    "opmode2": ["Abtauen", "Defrosting", "Defrosting", "Defrosting", "Defrosting"],
    "opmode3": ["Abtaupuffer", "Load defr. puffer", "Load defr. puffer", "Load defr. puffer", "Load defr. puffer"],
    "opmode4": ["WW Puffer", "DHW loading", "DHW loading", "DHW loading", "DHW loading"],
    "opmode5": ["Speicherenergie", "Storage energy", "Storage energy", "Storage energy", "Storage energy"],
    "opmode6": ["Heizen", "Heating", "Chauffage", "Riscald.", "Verwarmen"],
    "opmode7": ["KÃ¼hlen", "Cooling", "Refroidissement", "Raffredd.", "Koelen"],
    "opmode8": ["Pool", "Pool", "Pool", "Pool", "Pool"],
    "opmode9": ["UmwÃ¤lzung", "Idle", "Idle" , "Idle" , "Idle"],
    "opmode10": ["Standby", "Standby", "Standby", "Standby", "Standby"],
    "opmode11": ["Estrichtrockung", "Screed drying", "Screed drying", "Screed drying", "Screed drying"],
    "opmode12": ["Frostschutz", "Frost protection", "Frost protection", "Frost protection", "Frost protection"],
    "opmode13": ["PrÃ¼fbetrieb", "Test mode", "Test mode", "Test mode", "Test mode"],
    "opmode14": ["Sperrsignal", "Blocking signal", "Blocking signal", "Blocking signal", "Blocking signal"],
    "opmode15": ["Hygienefunktion", "Hygiene function", "Hygiene function", "Hygiene function", "Hygiene function"],
    "opmode16": ["Silent Modus", "Silent mode", "Silent mode", "Silent mode", "Silent mode"],
}
