import csv
import math


BASELINE = 250
THRESHOLD = 50


def magnetic_magnitude(x, y, z):
    return math.sqrt(x*2 + y2 + z*2)


with open("data/magnetic_readings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x = float(row["x"])
        y = float(row["y"])
        z = float(row["z"])

        magnitude = magnetic_magnitude(x, y, z)

        difference = abs(magnitude - BASELINE)

        if difference > THRESHOLD:
            print(
                f"Time {row['time']}: "
                f"ANOMALY DETECTED | "
                f"Magnetic field = {magnitude:.2f}"
            )
        else:
            print(
                f"Time {row['time']}: "
                f"Normal | "
                f"Magnetic field = {magnitude:.2f}"
            )
