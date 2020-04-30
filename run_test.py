from run_commands import run_simulation

"""
    This file contains the function for running the test.

    - The first line of test file contains the steps.
    - The second line contains the expected result (outcome).
"""


def run_test(test, car):
    line_count = 0
    with open(test) as test_file:
        for line in test_file:
            line_count += 1  # returns current line numbeer
            if line_count == 1:
                list_of_commands = line.split()
                result = run_simulation(list_of_commands, car)
            if line_count == 2:
                print('Measured =?= Expected')
                print(f'{str(result)} =?= {line}')
                if line == str(result):
                    print('PASSED TEST')
                else:
                    print('FAILED TEST')
