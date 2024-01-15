# Given values
velocity = 80  # in km/h
mass = 1500  # in kg
drag_coefficient = 0.31
cross_sectional_area = 1.97  # in m²
rolling_resistance_coefficient = 0.015
temperature = 20  # in °C
air_density = 1.225  # kg/m³ (standard air density at sea level at 15°C)
g = 9.81  # acceleration due to gravity in m/s²

# Convert velocity from km/h to m/s
velocity = velocity * (1000 / 3600)

# Calculate aerodynamic drag force
drag_force = 0.5 * drag_coefficient * air_density * cross_sectional_area * velocity**2

# Calculate rolling resistance force
rolling_resistance_force = rolling_resistance_coefficient * mass * g

# Calculate gravitational force
gravity_force = mass * g

# Calculate total force
total_force = drag_force + rolling_resistance_force + gravity_force

# Calculate power consumption
power_consumption = total_force * velocity

# Display the result
print(f"The power consumption of the vehicle is: {power_consumption} Watts")
