import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Simulated drone flight path
# -----------------------------

drone_x = np.linspace(0, 10, 100)
drone_y = 5 + 2 * np.sin(drone_x)

# -----------------------------
# Simulated magnetic field
# -----------------------------

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

X, Y = np.meshgrid(x, y)

magnetic_field = 250 * np.ones_like(X)

# Simulated metallic anomalies
anomaly1 = 120 * np.exp(-((X - 3)*2 + (Y - 4)*2) / 0.5)
anomaly2 = 180 * np.exp(-((X - 7)*2 + (Y - 6)*2) / 0.4)
anomaly3 = 100 * np.exp(-((X - 8)*2 + (Y - 2)*2) / 0.5)

magnetic_field += anomaly1 + anomaly2 + anomaly3

# -----------------------------
# Display dashboard
# -----------------------------

plt.figure(figsize=(12, 8))

plt.contourf(
    X,
    Y,
    magnetic_field,
    levels=40
)

plt.colorbar(label="Magnetic Field Strength")

# Drone flight path
plt.plot(
    drone_x,
    drone_y,
    linestyle="--",
    linewidth=2,
    label="Drone Flight Path"
)

# Detected anomalies
anomaly_locations = [
    (3, 4),
    (7, 6),
    (8, 2)
]

for ax, ay in anomaly_locations:
    plt.scatter(
        ax,
        ay,
        marker="X",
        s=180,
        label="Detected Metallic Anomaly"
    )

plt.title(
    "Drone-Based Intelligent Magnetic Sensing System"
)

plt.xlabel("Survey Area X")
plt.ylabel("Survey Area Y")

plt.legend()

plt.text(
    0.5,
    10.5,
    "DRONE STATUS: ACTIVE   |   ANOMALIES DETECTED: 3",
    fontsize=12
)

plt.tight_layout()

plt.show()
