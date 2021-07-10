from run_commands import run_simulation
from vehicle import Vehicle

"""
    This file contains the function for running the test.

    - The first line of test file contains the steps.
    - The second line contains the expected result (outcome).
"""

def read_test(test: str) -> list[str]:
    with open(test) as test_file:
        test_lines = test_file.readlines()
    test_commands = test_lines[:-2]
    test_exp_result = test_lines[-1]
    return test_commands, test_exp_result

def assert_result(exp_res: str, res: bool) -> None:
    print('Measured =?= Expected')
    print(f'{exp_res} =?= {res}')
    if str(exp_res) == str(res):
        print('PASSED TEST')
    else:
        print('FAILED TEST')


def run_test(test: str, car: Vehicle) -> None:
    test_commands, test_exp_result = read_test(test)
    result = run_simulation(test_commands, car)
    assert_result(test_exp_result, result)
