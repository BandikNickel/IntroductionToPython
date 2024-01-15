# Define a list of vehicles with their attributes
vehicles = [
    {"name": "Vehicle A", "mass": 1500, "rolling_resistance_coefficient": 0.015, "drag_coefficient": 0.31, "cross_sectional_area": 1.97, "velocity_kmh": 80},
    {"name": "Vehicle B", "mass": 1800, "rolling_resistance_coefficient": 0.018, "drag_coefficient": 0.35, "cross_sectional_area": 2.2, "velocity_kmh": 75},
    {"name": "Vehicle C", "mass": 1300, "rolling_resistance_coefficient": 0.012, "drag_coefficient": 0.28, "cross_sectional_area": 1.8, "velocity_kmh": 90},
]

# Constants
g = 9.81  # m/s²
air_density = 1.225  # kg/m³
efficiency_threshold = 10000  # 10 kW

# Calculate power consumption for each vehicle and check efficiency
for vehicle in vehicles:
    mass = vehicle["mass"]
    rolling_resistance_coefficient = vehicle["rolling_resistance_coefficient"]
    drag_coefficient = vehicle["drag_coefficient"]
    cross_sectional_area = vehicle["cross_sectional_area"]
    velocity_kmh = vehicle["velocity_kmh"]

    # Convert velocity to m/s
    velocity_ms = velocity_kmh * 1000 / 3600

    # Calculate rolling resistance force
    rolling_resistance_force = rolling_resistance_coefficient * mass * g

    # Calculate air resistance force
    air_resistance_force = 0.5 * air_density * drag_coefficient * cross_sectional_area * velocity_ms**2

    # Calculate total power consumption
    power_consumption = (rolling_resistance_force + air_resistance_force) * velocity_ms

    # Check if the vehicle is energy-efficient
    is_efficient = power_consumption <= efficiency_threshold

    print(f"{vehicle['name']} - Power Consumption: {power_consumption:.2f} watts")
    if is_efficient:
        print(f"{vehicle['name']} is energy-efficient.\n")
    else:
        print(f"{vehicle['name']} is not energy-efficient.\n")
