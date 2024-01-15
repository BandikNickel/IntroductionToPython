# vehicle_module.py
import json
from pathlib import Path

class Vehicle:
    def __init__(self, vehicle_type, mass, rolling_resistance_coefficient, drag_coefficient, cross_sectional_area):
        self.type = vehicle_type
        self.mass = mass
        self.rolling_resistance_coefficient = rolling_resistance_coefficient
        self.drag_coefficient = drag_coefficient
        self.cross_sectional_area = cross_sectional_area

def calculate_power_consumption(vehicle):
    g = 9.81  # m/s²
    air_density = 1.225  # kg/m³

    # For simplicity, assume constant velocity of 80 km/h for all vehicles
    velocity_kmh = 80
    # Convert velocity to m/s
    velocity_ms = velocity_kmh * 1000 / 3600

    # Calculate rolling resistance force
    rolling_resistance_force = vehicle.rolling_resistance_coefficient * vehicle.mass * g

    # Calculate air resistance force
    air_resistance_force = 0.5 * air_density * vehicle.drag_coefficient * vehicle.cross_sectional_area * velocity_ms**2

    # Calculate total power consumption
    power_consumption = (rolling_resistance_force + air_resistance_force) * velocity_ms

    return power_consumption

def read_vehicle_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            vehicles = [Vehicle(**vehicle_data) for vehicle_data in data]
        return vehicles
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return []
    
 Power_Threshold = 10_000
is_efficient = power_consumption <= efficiency_threshold

read_vehicle_data_from_json(Path(__file__).parent / "vehicles.json")
print(f"Vehicle: {Vehicle} | Power Consumption: {vehicle.calculate_power_consumption():.2f}W | energy-efficient: {is_efficient}")         


def check_energy_efficiency(vehicle):
    efficiency_threshold = 10000  # 10 kW
    power_consumption = calculate_power_consumption(vehicle)
    return power_consumption <= efficiency_threshold
