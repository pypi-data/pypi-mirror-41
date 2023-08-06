import tempfile

DEFAULT_FILES_DIR = tempfile.gettempdir() + "/vaillant_vr900_files"

DEFAULT_COOKIE_FILE_NAME = "/.vr900-vaillant.cookies"
DEFAULT_SERIAL_NUMBER_FILE_NAME = "/.vr900-vaillant.serial"

DEFAULT_SMARTPHONE_ID = "vr900-connector"

DEFAULT_BASE_URL = "https://smart.vaillant.com/mobile/api/v4"
TEST_LOGIN_URL = "/account/user/v1/details"
REQUEST_NEW_TOKEN_URL = "/account/authentication/v1/token/new"
AUTHENTICATE_URL = "/account/authentication/v1/authenticate"

FACILITIES_URL = "/facilities"
ROOMS_URl = "/facilities/{serialNumber}/rbr/v1/rooms"
ROOM_TIMEPROGRAM_URL = "/facilities/{serialNumber}/rbr/v1/rooms/{index}/timeprogram"
ZONES_URL = "/facilities/{serialNumber}/systemcontrol/v1/zones"
DHW_URL = "/facilities/{serialNumber}/systemcontrol/v1/dhw/{id}/hotwater"
DHW_SETPOINT_TEMPERATURE_URL = DHW_URL + '/configuration/temperature_setpoint'
DHW_SET_OPERATION_MODE_URL = DHW_URL + '/configuration/operation_mode'
CIRCULATION_URL = "/facilities/{serialNumber}/systemcontrol/v1/dhw/{id}/circulation"
HVAC_STATE_URL = "/facilities/{serialNumber}/hvacstate/v1/overview"
SYSTEM_STATUS_URL = "/facilities/{serialNumber}/system/v1/status"
SYSTEM_CONTROL_URL = "/facilities/{serialNumber}/systemcontrol/v1"
LIVE_REPORT_URL = "/facilities/{serialNumber}/livereport/v1"
QUICK_MODE_URL = SYSTEM_CONTROL_URL + "/configuration/quickmode"
CURRENT_PV_METERING_INFO_URL = '/facilities/{serialNumber}/spine/v1/currentPVMeteringInfo'
EMF_URL = '/facilities/{serialNumber}/emf/v1/devices'
REPEATERS_URL = '/facilities/{serialNumber}/rbr/v1/repeaters'

HOLIDAY_MODE = 'HOLIDAY'
QM_HOTWATER_BOOST = 'QM_HOTWATER_BOOST'
QM_VENTILATION_BOOST = 'QM_VENTILATION_BOOST'
QM_ONE_DAY_AWAY = 'QM_ONE_DAY_AWAY'
QM_SYSTEM_OFF = 'QM_SYSTEM_OFF'
QM_ONE_DAY_AT_HOME = 'QM_ONE_DAY_AT_HOME'
QM_PARTY = 'QM_PARTY'

CIRCULATION_MODE_OFF = 'OFF'
CIRCULATION_MODE_ON = 'ON'
CIRCULATION_MODE_AUTO = 'AUTO'
CIRCULATION_MODE_AUTO_OFF = 'AUTO_OFF'
CIRCULATION_MODE_AUTO_ON = 'AUTO_ON'

HOT_WATER_MODE_AUTO = 'AUTO'
HOT_WATER_MODE_AUTO_OFF = 'AUTO_OFF'
HOT_WATER_MODE_AUTO_ON = 'AUTO_ON'
HOT_WATER_MODE_OFF = 'OFF'
HOT_WATER_MODE_ON = 'ON'
HOT_WATER_MODES = [HOT_WATER_MODE_AUTO, HOT_WATER_MODE_ON, HOT_WATER_MODE_OFF, QM_HOTWATER_BOOST]
HOT_WATER_MIN_TEMP = 35
HOT_WATER_MAX_TEMP = 70


THERMOSTAT_QUICK_VETO = "QUICK_VETO"
THERMOSTAT_ROOM_MODE_AUTO = 'AUTO'
THERMOSTAT_ROOM_MODE_AUTO_ON = 'AUTO_ON'
THERMOSTAT_ROOM_MODE_AUTO_OFF = 'AUTO_OFF'
THERMOSTAT_ROOM_MODE_OFF = 'OFF'
THERMOSTAT_ROOM_MODE_MANUAL = 'MANUAL'
THERMOSTAT_ROOM_MODES = [THERMOSTAT_ROOM_MODE_AUTO, THERMOSTAT_ROOM_MODE_OFF, THERMOSTAT_ROOM_MODE_MANUAL,
                         THERMOSTAT_QUICK_VETO]

THERMOSTAT_ZONE_MODE_OFF = 'OFF'
THERMOSTAT_ZONE_MODE_DAY = 'DAY'
THERMOSTAT_ZONE_MODE_NIGHT = 'NIGHT'
THERMOSTAT_ZONE_MODE_AUTO = 'AUTO'

THERMOSTAT_ZONE_MODES = [THERMOSTAT_ZONE_MODE_AUTO, THERMOSTAT_ZONE_MODE_OFF, THERMOSTAT_ZONE_MODE_DAY,
                         THERMOSTAT_ZONE_MODE_NIGHT, THERMOSTAT_QUICK_VETO]

THERMOSTAT_MAX_TEMP = 30
FROST_PROTECTION_TEMP = 5
