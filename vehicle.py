import config as cf

"""
    This file contains the definition of the vehicle class.
"""


class vehicle():
    def __init__(self):
        # initializing variables
        self.ignition = 'OFF'
        self.speed = 0
        self.temp = cf.NORMAL_TEMP
        self.error = 'NORMAL_QOS'
        self.commands = 0
        self.debug = True

    def set_ignition(self, on_off):
        self.commands += 1
        if on_off in cf.IGNITION_STATE:
            self.ignition = on_off
        else:
            raise KeyError
        if self.debug:
            print(f'{self.commands}. Ignition: {self.ignition}')

    def set_speed(self, speed):
        self.commands += 1
        if speed >= 0 and self.error == 'NORMAL_QOS' and self.ignition == 'ON':
            self.speed = speed
        else:
            print(f'Unable to set speed due to {self.error}')
        if self.debug:
            print(f'{self.commands}. Speed: {self.speed}')
        self.check_state()

    def set_temp(self, temp):
        self.commands += 1
        if self.ignition == 'ON':
            self.temp = temp
        if self.debug:
            print(f'{self.commands}. Temperature: {self.temp}')
        self.check_state()

    def set_error(self, error):
        if error in cf.QOS:
            self.error = error
            # print(f'ERROR STATE! {self.error}')
        else:
            raise KeyError

    def check_state(self):
        if self.speed >= cf.SPEED_LIMIT:
            self.set_error('SPEED_ERROR_QOS')
        elif self.temp >= cf.TEMP_LIMIT:
            self.set_error('TEMP_ERROR_QOS')
        else:
            self.set_error('NORMAL_QOS')
        if self.error != 'NORMAL_QOS':
            print(f'ERROR STATE! {self.error}')

    def print_state(self):
        print('------------STATE------------')
        print(f'Ignition:    {self.ignition}')
        print(f'Temperature: {self.temp}')
        print(f'Speed:       {self.speed}')
        print(f'Error state: {self.error}')
        print('-----------------------------')

    def check_simulation_end(self):
        if self.error == 'NORMAL_QOS' and self.speed == 0 and self.ignition == 'OFF':
            return True
        else:
            return False, self.error
