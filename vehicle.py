from config import QOS, IGNITION_STATE, NORMAL_TEMP, SPEED_LIMIT, TEMP_LIMIT

"""
    This file contains the definition of the vehicle class.
"""


class Vehicle():
    def __init__(self):
        # initializing variables
        self.ignition = IGNITION_STATE.OFF
        self.speed = 0
        self.temp = NORMAL_TEMP
        self.error = QOS.NORMAL
        self.commands = 0
        self.debug = True

    def set_ignition(self, on_off: IGNITION_STATE):
        self.commands += 1
        if isinstance(on_off, IGNITION_STATE):
            self.ignition = on_off
        else:
            raise KeyError
        if self.debug:
            print(f'{self.commands}. Ignition: {self.ignition}')

    def set_speed(self, speed: int):
        self.commands += 1
        if speed >= 0 and self.error == QOS.NORMAL and self.ignition == IGNITION_STATE.ON:
            self.speed = speed
        else:
            print(f'Unable to set speed due to {self.error}')
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
            print(f'ERROR STATE! {self.error}')

    def print_state(self):
        print('------------STATE------------')
        print(f'Ignition:    {self.ignition}')
        print(f'Temperature: {self.temp}')
        print(f'Speed:       {self.speed}')
        print(f'Error state: {self.error}')
        print('-----------------------------')

    def check_simulation_end(self):
        if self.error == QOS.NORMAL and \
           self.speed == 0 and \
           self.ignition == IGNITION_STATE.OFF:
            return True
        else:
            return False, self.error
