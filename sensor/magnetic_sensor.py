import math


def calculate_magnetic_field(x, y, z):
    """
    Calculate the total magnetic field strength
    from X, Y and Z axis measurements.
    """
    magnitude = math.sqrt(x*2 + y2 + z*2)
    return magnitude


def check_anomaly(magnitude, baseline, threshold=50):
    """
    Check whether the measured magnetic field
    differs significantly from the baseline.
    """
    difference = abs(magnitude - baseline)

    if difference > threshold:
        return True

    return False


# Example sensor readings
x = 120
y = 80
z = 200

magnetic_field = calculate_magnetic_field(x, y, z)

# Example normal/background magnetic field
baseline = 245

anomaly = check_anomaly(magnetic_field, baseline)

print("Magnetic Field Strength:", round(magnetic_field, 2))

if anomaly:
    print("⚠️ Magnetic anomaly detected!")
else:
    print("Normal magnetic field.")
