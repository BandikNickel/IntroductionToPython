# main_script.py
from vehicle_module import Vehicle, calculate_power_consumption

def check_energy_efficiency(vehicle):
    efficiency_threshold = 10000  # 10 kW
    power_consumption = calculate_power_consumption(vehicle)
    return power_consumption <= efficiency_threshold

def main():
    vehicles = [
        Vehicle("Vehicle A", 1500, 0.015, 0.31, 1.97, 80),
        Vehicle("Vehicle B", 1800, 0.018, 0.35, 2.2, 75),
        Vehicle("Vehicle C", 1300, 0.012, 0.28, 1.8, 90),
    ]

    for vehicle in vehicles:
        power_consumption = calculate_power_consumption(vehicle)
        efficient = check_energy_efficiency(vehicle)

        print(f"{vehicle.name} - Power Consumption: {power_consumption} watts")
        if efficient:
            print(f"{vehicle.name} is energy-efficient.\n")
        else:
            print(f"{vehicle.name} is not energy-efficient.\n")

if __name__ == "__main__":
    main()
