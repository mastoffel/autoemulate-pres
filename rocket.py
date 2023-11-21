import numpy as np
def rocket_simulator(params):
    angle, thrust = params
    angle_rad = np.radians(angle)  # Convert angle to radians

    # Constants
    g = 9.81  # Gravity (m/s^2)
    mass = 50.0  # Mass of the rocket (kg), assumed constant
    air_resistance_coeff = 0.01  # Air resistance coefficient, assumed simple

    # Initial conditions
    velocity = thrust / mass
    vx = velocity * np.cos(angle_rad)
    vy = velocity * np.sin(angle_rad)
    max_altitude = 0
    x = 0
    y = 0
    t = 0
    dt = 0.1  # Time step (s)

    # Simulation loop
    while vy >= 0:  # Simulate until the rocket starts descending
        # Update velocities
        vx -= air_resistance_coeff * vx * dt
        vy -= (g + air_resistance_coeff * vy) * dt

        # Update position
        x += vx * dt
        y += vy * dt
        max_altitude = max(max_altitude, y)

        t += dt

    return max_altitude