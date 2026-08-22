import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Drone Magnetic Anomaly Detection",
    layout="wide"
)

st.title("🚁 Drone-Based Magnetic Sensing System")
st.write("Visual prototype for metallic anomaly detection")

st.subheader("Drone & Sensor Input")

altitude = st.number_input(
    "Drone altitude above ground (m)",
    min_value=1.0,
    value=20.0
)

magnetic_value = st.number_input(
    "Magnetic field reading (µT)",
    min_value=0.0,
    value=85.0
)

threshold = st.number_input(
    "Detection threshold (µT)",
    min_value=0.0,
    value=60.0
)

scan_distance = st.number_input(
    "Scan distance (m)",
    min_value=1.0,
    value=50.0
)

if st.button("🔍 DETECT ANOMALY"):

    st.subheader("Detection Result")

    if magnetic_value > threshold:

        st.error("⚠️ METALLIC ANOMALY DETECTED")

        st.write(f"*Drone altitude:* {altitude} m")
        st.write(f"*Magnetic field:* {magnetic_value} µT")
        st.write(f"*Threshold:* {threshold} µT")
        st.write(f"*Scan distance:* {scan_distance} m")

        st.success("Anomalous magnetic field detected below the drone.")

        # Visual representation
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.set_xlim(0, scan_distance)
        ax.set_ylim(-10, altitude + 10)

        # Ground
        ax.axhline(0, linewidth=3)

        # Drone
        drone_x = scan_distance / 2
        ax.scatter(drone_x, altitude, s=500, marker="^")
        ax.text(
            drone_x,
            altitude + 2,
            "DRONE",
            ha="center"
        )

        # Anomaly
        anomaly_x = drone_x
        anomaly_depth = -5

        ax.scatter(
            anomaly_x,
            anomaly_depth,
            s=300,
            marker="X"
        )

        ax.text(
            anomaly_x + 2,
            anomaly_depth,
            "METALLIC\nANOMALY",
            va="center"
        )

        ax.set_xlabel("Scan distance (m)")
        ax.set_ylabel("Height / depth (m)")
        ax.set_title("Drone Magnetic Anomaly Visualization")

        st.pyplot(fig)

    else:

        st.success("✅ NO METALLIC ANOMALY DETECTED")

        st.write(f"*Drone altitude:* {altitude} m")
        st.write(f"*Magnetic field:* {magnetic_value} µT")
        st.write(f"*Threshold:* {threshold} µT")

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.set_xlim(0, scan_distance)
        ax.set_ylim(-10, altitude + 10)

        ax.axhline(0, linewidth=3)

        drone_x = scan_distance / 2

        ax.scatter(
            drone_x,
            altitude,
            s=500,
            marker="^"
        )

        ax.text(
            drone_x,
            altitude + 2,
            "DRONE",
            ha="center"
        )

        ax.set_xlabel("Scan distance (m)")
        ax.set_ylabel("Height / depth (m)")
        ax.set_title("Drone Scan — No Anomaly Detected")

        st.pyplot(fig)
