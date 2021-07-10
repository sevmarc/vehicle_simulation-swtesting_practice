from vehicle import Vehicle
from config import *
"""
    This file contains the run simulation function.
"""


def run_simulation(command_list: list[str], car: Vehicle()):
    for com in command_list:
        print(f'Running command: {com}')
        eval(f'car.{com}')
    print('==============================RESULT=============================')
    car.print_state()
    result = car.check_simulation_end()
    print(result, '\n')
    return result
