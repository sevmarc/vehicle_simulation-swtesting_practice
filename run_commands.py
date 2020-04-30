"""
    This file contains the run simulation function.
"""


def run_simulation(command_list, car):
    for i in range(1, len(command_list)):  # the 0 command is the simulation.py
        cd = command_list[i]
        print(f'Running command: {cd}')
        eval(f'car.{cd}')
    print('==============================RESULT=============================')
    car.print_state()
    result = car.check_simulation_end()
    print(result)
    print('\n')
    return result
