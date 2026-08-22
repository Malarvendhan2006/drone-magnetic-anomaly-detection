import math
import matplotlib.pyplot as plt

# Simulated drone flight path
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7]

# Simulated magnetic-field strength
magnetic_values = [
    245, 248, 247, 250, 249,
    252, 310, 360, 325, 250, 248
]

BASELINE = 250
THRESHOLD = 50

normal_x = []
normal_y = []

anomaly_x = []
anomaly_y = []

for i in range(len(magnetic_values)):

    difference = abs(magnetic_values[i] - BASELINE)

    if difference > THRESHOLD:
        anomaly_x.append(x[i])
        anomaly_y.append(y[i])
    else:
        normal_x.append(x[i])
        normal_y.append(y[i])

# Plot drone flight path
plt.figure(figsize=(10, 7))

plt.plot(
    x,
    y,
    linestyle="--",
    marker="o",
    label="Drone Flight Path"
)

# Normal readings
plt.scatter(
    normal_x,
    normal_y,
    s=80,
    label="Normal Magnetic Field"
)

# Anomalies
plt.scatter(
    anomaly_x,
    anomaly_y,
    s=150,
    marker="X",
    label="Magnetic Anomaly"
)

plt.title("Drone-Based Magnetic Anomaly Detection")
plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.grid(True)
plt.legend()

plt.show()
