# STEM Series: Apollo 11 Lunar Module Descent Simulation

This Python script simulates the descent of the Apollo 11 Lunar Module to the moon's surface. It's a great example of how coding and STEM (Science, Technology, Engineering, Mathematics) come together!

## Script Breakdown

The script uses the `matplotlib` library to create a plot of the Lunar Module's height over time.

### Constants

The script starts by defining some constants:

- `g`: The gravity on the moon, in meters per second squared (m/s^2).
- `burn_rate`: The rate at which the Lunar Module's engine burns fuel, in kilograms per second (kg/s).
- `thrust`: The force produced by the Lunar Module's engine, in newtons (N).
- `mass`: The initial mass of the Lunar Module, in kilograms (kg).
- `height`: The initial height of the Lunar Module above the moon's surface, in meters (m).
- `velocity`: The initial horizontal velocity of the Lunar Module, in meters per second (m/s).

### Variables

Next, the script initializes some variables:

- `t`: The current time, in seconds (s).
- `dt`: The time step, in seconds (s). This is how much time passes in each iteration of the simulation.
- `fuel`: The amount of fuel remaining, in kilograms (kg).
- `v`: The Lunar Module's vertical velocity, in meters per second (m/s).
- `h`: The Lunar Module's current height above the moon's surface, in meters (m).

### Simulation

The script then enters a loop that continues until the Lunar Module lands (i.e., its height `h` reaches 0). In each iteration of the loop, the script:

- Calculates the force, acceleration, velocity, and height of the Lunar Module.
- Decreases the amount of fuel and the mass of the Lunar Module.
- Stores the current time and height for later plotting.

### Plotting

Finally, the script plots the Lunar Module's height over time using `matplotlib`. The x-axis represents time in seconds, and the y-axis represents height in meters.

## Running the Script

To run the script, you'll need Python and `matplotlib` installed on your computer. Then, you can run the script from the command line like this:

```bash
python3 lunar_module_descent.py
