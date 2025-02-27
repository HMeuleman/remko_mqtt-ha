# Remko generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4

# Query list
#query_list = []
#query_list = [127, 132, 327, 1014, 1088, 1893, 1894, 1946, 1951, 2015, 5001, 5032, 5036, 5123, 5039, 5190, 5320, 5693, 5822, 5824]
query_list = [1014, 1088, 1666, 1893, 1894, 1946, 2015, 5001, 5032, 5036, 5123, 5190, 5320, 5693, 5822, 5824]
client_id = "xxx"

#min_work_temp, WP will not work when 'outside temp' below this temp. Goes into frost protection state
# Register as sensors
reg_id = {
    #  reg_id: ['reg#', 'type', 'unit', 'min', 'max'],
    "language": ["1014", "string", "", "", ""],
    #"version": ["327", "number", "", "" , "" ],
    #"user_level": ["5029", "string", "", "", ""],
    #"dhw_opmode": ["1079", "select_input", "", 0, 16],
    #"water_temp_req": ["1082", "temperature_input", "ºC", 20.0, 60.0],
    "min_work_temp": ["1666", "temperature_input", "ºC", -20.0, 20.0],
    "temp_req": ["1946", "temperature_input", "ºC", -10.0, 10.0],
    "absence_mode": ["1893", "switch", "", "", ""],
    "party_mode": ["1894", "switch", "", "", ""],
    "main_mode": ["1088", "select_input", "", "", ""],
    "opmode": ["5001", "sensor_mode", "", "", ""],
    "out_temp": ["5032", "temperature", "ºC", 0, 40],
    "out_temp_corr": ["2015", "temperature_input", "ºC", -10.0, 10.0],
    "floor_temp": ["5036", "temperature", "ºC", 0, 70],
    "return_floor_temp": ["5123", "temperature", "ºC", 0, 70],
    "verw_water_temp": ["5190", "temperature", "ºC", 0, 70],
    "el_consumption": ["5320", "sensor_el", "W", 0, 6000],
    "energy_heating": ["5374", "sensor_en", "kWh", "", ""],
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
    "min_work_temp": ["min. Außentemperatur", "Min. outside temperature", "Min. outside temperature", "Temperatura esterna min.", "Min. buiten temperatuur"],
    "temp_req": ["Kälter / Wärmer", "Colder / hotter", "Plus froid / Plus chaud", "Più freddo / più caldo", "Kouder / Warmer"],
    "out_temp": ["Außentemperatur", "Outside temperature", "Température extérieure", "Temp. esterna", "Buitentemperatuur"],
    "out_temp_corr": ["Außentemperatur S10", "Outside temperature S10", "Température extérieure S10", "Temp. Esterna S10", "Buitentemperatuur S10"],
    "floor_temp": ["Ist-Temperatur", "Actual temperature", "Température réelle", "Temp. Circ.", "Vloerverwarming temp."],
    "return_floor_temp": ["Rücklauftemp", "Return temp.", "Temp. retour", "Temp. ritorno", "Vloerverwarming retour temp."],
    "verw_water_temp": ["Heizwasser Ist-Temp.", "Heating water temp. (actual)", "Temp. eau chaude (Val.r réelle)", "Temp. Produzione", "Verw. watertemp (act. waarde)"],
    "el_consumption": ["Leistung elektrisch", "electr. power heatpump", "Puissance électr. thermopompe", "Ass. elettrico PDC", "Elektr. Vermogen warmtepomp"],
    "energy_heating": ["Energie Heizen", "Energy heating", "Énergie Chauffer", "Energia riscaldamento", "Energie verwarmen"],
    "main_mode": ["Raumklima Modus", "Room climate mode", "Mode de climat ambiant", "Modalità Clima ambiente", "Ruimteklimaat-Modus"],
    "opmode": ["Aktuelle Betriebsart", "Current operating mode", "Mode de fonctionnement actuel", "Modo operativo attuale", "Actuele bedrijfstoestand"],
    #"dhw_opmode": ["Modus", "Mode", "Mode", "Modo funzionamento", "Modus"],
    "absence_mode": ["Abwesenheitsmodus", "Absence mode", "Mode d'absence", "Modalità Assenza", "Afwezig mode"],
    "party_mode": ["Partymodus", "Party mode", "Mode de fête", "Modalità Party", "Partymodus"],
    "dhw_heating": ["1x WW aufheizen", "1x DHW heating", "1x WW Chauffage", "Riscaldare 1 x AC", "1x WW Opwarmen"],
    "comp_starts": ["Kompressorstarts", "Compressor starts", "Démarrages de compresseurs", "Avviamenti compressore", "Compressor opstarts"],
    "comp_hours": ["Laufzeit (Stunden)", "Runtime (hours)", "Durée (heures)", "Ore funzionamento", "Looptijd (uren)"],
    "mode1": ["Auto", "Auto", "Auto", "Auto", "Auto"],
    "mode2": ["Heizen", "Heating", "Chauffage", "Riscald.", "Verwarmen"],
    "mode3": ["Standby", "Standby", "Standby", "Standby", "Standby"],
    "mode4": ["Kühlen", "Cooling", "Refroidissement", "Raffredd.", "Koelen"],
    "dhwopmode0": ["Automatik Komfort", "Automatic comfort", "Automatic comfort", "Automatic comfort", "Automatisch comfort"],
    "dhwopmode1": ["Automatik Eco", "Automatic eco", "Automatic eco", "Automatic eco", "Automatisch eco"],
    "dhwopmode2": ["Nur Solar/PV", "Solar/PV only", "Solar/PV only", "Solar/PV only", "Zonnepanelen enkel", ],
    "dhwopmode3": ["Aus", "Off", "Off", "Off", "Uit"],
    "opmode1": ["Störung", "Forced off", "Forced off", "Forced off", "Forced off"],
    "opmode2": ["Abtauen", "Defrosting", "Defrosting", "Defrosting", "Defrosting"],
    "opmode3": ["Abtaupuffer", "Load defr. puffer", "Load defr. puffer", "Load defr. puffer", "Load defr. puffer"],
    "opmode4": ["WW Puffer", "DHW loading", "DHW loading", "DHW loading", "DHW loading"],
    "opmode5": ["Speicherenergie", "Storage energy", "Storage energy", "Storage energy", "Storage energy"],
    "opmode6": ["Heizen", "Heating", "Chauffage", "Riscald.", "Verwarmen"],
    "opmode7": ["Kühlen", "Cooling", "Refroidissement", "Raffredd.", "Koelen"],
    "opmode8": ["Pool", "Pool", "Pool", "Pool", "Pool"],
    "opmode9": ["Umwälzung", "Idle", "Idle" , "Idle" , "Idle"],
    "opmode10": ["Standby", "Standby", "Standby", "Standby", "Standby"],
    "opmode11": ["Estrichtrockung", "Screed drying", "Screed drying", "Screed drying", "Screed drying"],
    "opmode12": ["Frostschutz", "Frost protection", "Protection anti-gel", "Antigelo", "Vorstbeveiliging"],
    "opmode13": ["Prüfbetrieb", "Test mode", "Test mode", "Test mode", "Test mode"],
    "opmode14": ["Sperrsignal", "Blocking signal", "Blocking signal", "Blocking signal", "Blocking signal"],
    "opmode15": ["Hygienefunktion", "Hygiene function", "Hygiene function", "Hygiene function", "Hygiene function"],
    "opmode16": ["Silent Modus", "Silent mode", "Silent mode", "Silent mode", "Silent mode"],
}
