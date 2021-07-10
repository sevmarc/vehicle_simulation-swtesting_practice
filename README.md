# vehicle_simulation-swtesting_practice
 This was submitted as the result of 'Testing and Software Quality' class of ELTE

## Project structure
### vehicle.py
Contains vehicle class definition, which defines the behavior of the simulation
#### config.py
The configuration file for the vehicle

### simulation.py
This is the runnable, which loads the simulation and the test inputs

### run_commands.py
Intermediary file between the vehicle and the test input

### run_test.py
Reads the test, and runs it

Goal: keyword based test cases
Instead of the 'python function calls', a new layer would be added, for example:
Old: set_speed(50)
New: SPEED 50

Old: set_ignition(IGNITION_STATE.ON)
New: IGNITION ON

The first word would be the function equivalent, the second the argument.

TODO:
- Keywords DSL needs a more stable system
- More tests
- Simulation mode, where live user input is evaluated, instead of test case as input