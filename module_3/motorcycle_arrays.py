import numpy as np

# laptimes are in seconds and miliseconds, but we'll use seconds for ease of use
lap_times = np.array([89.5, 88.3, 87.9, 89.2, 87.5]) 
best_lap = np.min(lap_times)
avg_lap_time = np.mean(lap_times)


print(f"Best Lap Time: {best_lap} sec")
print(f"Average Lap Time: {avg_lap_time:} sec")

fuel_levels = np.array([2.64, 2.25, 1.85, 1.45, 1.06])  # Fuel in liters
avg_fuel_consumption = (fuel_levels[0] - fuel_levels[-1]) / len(fuel_levels)

print(f"Average Fuel Consumption per Lap: {avg_fuel_consumption:.2f} L")

speeds = np.array([220, 225, 230, 228, 231])  # Speed in km/h
max_speed = np.max(speeds)
avg_speed = np.mean(speeds)

print(f"Max Speed: {max_speed} km/h")
print(f"Average Speed: {avg_speed:.2f} km/h")
