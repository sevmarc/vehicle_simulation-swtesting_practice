from enum import IntEnum

# parameter list

NORMAL_TEMP = 20
TEMP_LIMIT = 100
SPEED_LIMIT = 180

# Quality of State
class QOS(IntEnum):
    NORMAL = 1
    SPEED_ERROR = 2
    TEMP_ERROR = 3

# default ignition states (binary ON/OFF)
class IGNITION_STATE(IntEnum):
    ON = 1
    OFF = 2
