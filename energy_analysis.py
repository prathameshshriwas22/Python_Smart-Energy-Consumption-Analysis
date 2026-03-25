import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("energy_data.csv")

print("Energy Dataset\n")
print(data)

# average power
avg_power = data["power"].mean()
print("\nAverage Power Consumption:", avg_power)

# voltage check
if data["voltage"].max() > 235:
    print("Warning: High Voltage Detected")

# current check
if data["current"].max() > 6.5:
    print("Warning: High Current Detected")

# plot graph
plt.plot(data["time"], data["power"])
plt.xlabel("Time")
plt.ylabel("Power")
plt.title("Energy Consumption Analysis")
plt.show()