import numpy as np
import matplotlib.pyplot as plt

# Create a virtual survey area
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)

X, Y = np.meshgrid(x, y)

# Simulated background magnetic field
magnetic_field = 250 * np.ones_like(X)

# Simulated metallic anomalies
anomaly1 = 120 * np.exp(-((X - 3)*2 + (Y - 4)*2) / 0.8)
anomaly2 = 180 * np.exp(-((X - 7)*2 + (Y - 6)*2) / 0.6)
anomaly3 = 100 * np.exp(-((X - 8)*2 + (Y - 2)*2) / 0.5)

magnetic_field += anomaly1 + anomaly2 + anomaly3

# Display magnetic anomaly map
plt.figure(figsize=(10, 7))

plt.contourf(
    X,
    Y,
    magnetic_field,
    levels=30
)

plt.colorbar(label="Magnetic Field Strength")

plt.scatter(
    [3, 7, 8],
    [4, 6, 2],
    marker="X",
    s=150,
    label="Detected Anomaly"
)

plt.title("Simulated Magnetic Anomaly Map")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()

plt.show()
