import os

# Common constants
# =================================================================================
MAX_SCAN_SAMPLE_RATE = 1000000
JSON_EXTENSION = "json"
H5_EXTENSION = "h5"

# Raw data constants
# =================================================================================
DATA_FOLDER = "data"
DATA_FOLDER_REL_PATH = os.path.join(".", DATA_FOLDER)
RAW_DATA_FOLDER = "raw_data"
RAW_DATA_FOLDER_REL_PATH = os.path.join(DATA_FOLDER_REL_PATH, RAW_DATA_FOLDER)
RAW_DATA_FILE = "raw_data.h5"
RAW_DATA_FILE_REL_PATH = os.path.join(RAW_DATA_FOLDER_REL_PATH, RAW_DATA_FILE)

RAW_DATA_BUFFER_FILE_PREFIX = "raw_data_buffer_"
RAW_DATA_BUFFER_FILE_FORMAT = "raw_data_buffer_{}.h5"

# Logs constants
# =================================================================================
LOGS_FOLDER = "logs"
LOGS_FOLDER_REL_PATH = os.path.join(".", LOGS_FOLDER)
NANOCONTROL_LOG_FILE = "nanocontrol.log"
NANOCONTROL_LOG_FILE_REL_PATH = os.path.join(LOGS_FOLDER_REL_PATH, NANOCONTROL_LOG_FILE)

# Settings constants
# =================================================================================
SETTINGS_FOLDER = "settings"
SETTINGS_FOLDER_REL_PATH = os.path.join(".", SETTINGS_FOLDER)
SETTINGS_FILE = "settings.json"
SETTINGS_FILE_REL_PATH = os.path.join(SETTINGS_FOLDER_REL_PATH, SETTINGS_FILE)  # TODO: use
SETTINGS_PATH = "./settings/settings.json"

# JSON fields
SETTINGS_FIELD = "Settings"

DAQ_FIELD = "DAQ"
AI_FIELD = "AI"
AO_FIELD = "AO"

INTERFACE_TYPE_FIELD = "InterfaceType"
CONNECTION_CODE_FIELD = "ConnectionCode"

SAMPLE_RATE_FIELD = "SampleRate"
RANGE_ID_FIELD = "RangeId"
LOW_CHANNEL_FIELD = "LowChannel"
HIGH_CHANNEL_FIELD = "HighChannel"
INPUT_MODE_FIELD = "InputMode"
SCAN_FLAGS_FIELD = "ScanFlags"

# Calibration constants
# =================================================================================
CALIBRATION_PATH = "./settings/calibration.json"
DEFAULT_CALIBRATION_PATH = "./settings/default_calibration.json"

INFO_FIELD = "Info"

CALIBRATION_COEFFS_FIELD = "Calibration coeff"
U_TPL_FIELD = "Utpl"
T_TPL_FIELD = "Ttpl"
T_HTR_FIELD = "Thtr"
T_HTRD_FIELD = "Thtrd"
U_HTR_FIELD = "Uhtr"
I_HTR_FIELD = "Ihtr"
T_HEATER_FIELD = "Theater"
AMPLITUDE_CORRECTION_FIELD = "Amplitude correction"
R_HEATER_FIELD = "R heater"
HEATER_SAFE_VOLTAGE_FIELD = "Heater safe voltage"
CORR_FIELD = "corr"
# =================================================================================
