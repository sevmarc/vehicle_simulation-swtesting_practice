from config import QOS, IGNITION_STATE, NORMAL_TEMP, SPEED_LIMIT, TEMP_LIMIT

"""
    This file contains the definition of the vehicle class.
"""

KEYWORDS = {
    'IGNITION': 'set_ignition',
    'SPEED': 'set_speed',
    'TEMP': 'set_temp', 
    'STOP': 'check_simulation_end'
}
KEYWORDS_ARG = {
    'ON': IGNITION_STATE.ON,
    'OFF': IGNITION_STATE.OFF,
}

def decode_keyword(keyphrase: str):
    try:
        key, arg = keyphrase.split(' ')
    except ValueError:  # if keyphrase is one word ('STOP') -> arg is empty
        key, arg = keyphrase, ''
    arg = arg.strip('\n')
    try:
        if arg in KEYWORDS_ARG.keys():
            arg = KEYWORDS_ARG[arg]
        command_ = f'{KEYWORDS[key]}({str(arg)})'
    except KeyError:
        print('Incorrect keyword. ')
        return None
    return command_


class Vehicle():
    def __init__(self):
        # initializing variables
        self.ignition = IGNITION_STATE.OFF
        self.speed = 0
        self.temp = NORMAL_TEMP
        self.error = QOS.NORMAL
        self.commands = 0
        self.running = True
        self.debug = True

    def set_ignition(self, on_off: IGNITION_STATE):
        self.commands += 1
        if isinstance(on_off, IGNITION_STATE):
            self.ignition = on_off
            if self.ignition == IGNITION_STATE.OFF:  # ignition was turned off
                self.speed = 0
        else:
            raise KeyError
        if self.debug:
            print(f'{self.commands}. Ignition: {self.ignition.name}')

    def set_speed(self, speed: int):
        self.commands += 1
        if speed >= 0 and self.error == QOS.NORMAL and self.ignition == IGNITION_STATE.ON:
            self.speed = speed
        elif self.ignition == IGNITION_STATE.OFF:
            print(f'Unable to set speed: Ignition is in OFF state')
        else:
            print(f'Unable to set speed: {self.error.name}')
        if self.debug:
            print(f'{self.commands}. Speed: {self.speed}')
        self.check_state()

    def set_temp(self, temp: int):
        self.commands += 1
        if self.ignition == IGNITION_STATE.ON:
            self.temp = temp
        if self.debug:
            print(f'{self.commands}. Temperature: {self.temp}')
        self.check_state()

    def set_error(self, error: QOS):
        if error in QOS:
            self.error = error
            # print(f'ERROR STATE! {self.error}')
        else:
            raise KeyError

    def check_state(self):
        if self.speed >= SPEED_LIMIT:
            self.set_error(QOS.SPEED_ERROR)
        elif self.temp >= TEMP_LIMIT:
            self.set_error(QOS.TEMP_ERROR)
        else:
            self.set_error(QOS.NORMAL)
        if self.error != QOS.NORMAL:
            print(f'ERROR STATE! {self.error.name}')

    def print_state(self):
        print('------------STATE------------')
        print(f'Ignition:    {self.ignition.name}')
        print(f'Temperature: {self.temp}')
        print(f'Speed:       {self.speed}')
        print(f'Error state: {self.error.name}')
        print('-----------------------------')

    def check_simulation_end(self):
        self.running = False
        if self.error == QOS.NORMAL and \
           self.speed == 0 and \
           self.ignition == IGNITION_STATE.OFF:
            return True
        else:
            return False, self.error.name
