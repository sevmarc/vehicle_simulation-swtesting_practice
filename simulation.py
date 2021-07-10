from vehicle import Vehicle
from run_test import run_test
from run_commands import run_simulation
import datetime
import os
import sys

"""

The way the simulation works:
    - if parameters are a list of commands:test
      (command line: python simulation.py set_ignition('ON') set_speed(50)...)
      They are executed and the result is printed on console.
    - if first parameter is 'test' and second parameter is 'test file':
      A test log is created with results - only place of the log is on console.

"""

if __name__ == "__main__":
    test_mode = False
    # Can be run in test mode, first parameter: test, second: test file

    # we create the 'car' object for our simulation
    car = Vehicle()

    # test_mode or normal mode (simulation)
    def run(car):
        if test_mode:
            print('RUNNING TEST!')
            run_test(test_file, car)
        else:
            try:
                print('RUNNING SIMULATION!')
                while(car.running):
                    run_simulation(input(), car)
            # run_simulation(sys.argv, car)
            except KeyboardInterrupt():
                print('EXITING SIMULATION!')
                car.check_simulation_end()

    
    try:
        if sys.argv[1] == 'test':
            test_file = sys.argv[2]  # next parameter: test file
            test_name = test_file.rsplit('.')[0]
            test_file = 'test_cases/' + test_file
            test_mode = True
    except IndexError:
        pass

    # if we use test_mode, then the result is written in new testlog (logs folder)
    if test_mode:
        path = 'logs'
        try:
            os.mkdir(path)
        except OSError:
            pass
            # print ("Creation of the directory %s failed" % path)

        orig_stdout = sys.stdout
        b = str(datetime.datetime.now()).replace(" ", "_")
        b = b.replace(".", "_")
        b = b.replace(":", "_")
        b = test_name + '_' + b
        f = open(f'logs/{b}.txt', 'w')
        print(f'Test log can be accessed: logs/{b}.txt')
        sys.stdout = f


    run(car)  # running simulation

    # with test_mode, the file has to be closed and stdout reset
    if test_mode:
        sys.stdout = orig_stdout
        f.close()
