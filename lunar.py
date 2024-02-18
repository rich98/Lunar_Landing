import matplotlib.pyplot as plt

# Constants
g = 1.62  # Lunar gravity in m/s^2
burn_rate = 10  # Fuel burn rate in kg/s
thrust = 45000  # Thrust in N
mass = 15000  # Initial mass of the Lunar Module in kg
height = 50000  # Initial height in m
velocity = 1700  # Initial velocity in m/s (horizontal)

# Initialize variables
t = 0  # time
dt = 1  # time step
fuel = 8200  # amount of fuel in kg
v = 0  # vertical velocity in m/s
h = height  # current height in m

# Lists to store data for plotting
times = [t]
heights = [h]

while h > 0:
    # Calculate force, acceleration, velocity, and height
    if fuel > 0:
        F = thrust - mass * g
        fuel -= burn_rate * dt
    else:
        F = -mass * g
    a = F / mass
    v += a * dt
    h -= v * dt
    t += dt
    mass -= burn_rate * dt

    # Store data for plotting
    times.append(t)
    heights.append(h)

# Plot the data
plt.plot(times, heights)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Apollo 11 Lunar Module Descent Simulation')
plt.show()
