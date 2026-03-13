# Smart Food Quality Monitoring System
# Author: Sujitha Mary
# Description: Monitors gas level and temperature to detect food spoilage.

import serial
import time

# Connect to Arduino / ESP32 serial port
ser = serial.Serial('COM3', 9600)   # Change COM port if needed
time.sleep(2)

gas_threshold = 400
temp_threshold = 35

print("Food Quality Monitoring Started...")

while True:
    try:
        data = ser.readline().decode().strip()
        values = data.split(',')

        if len(values) == 2:
            gas_value = int(values[0])
            temperature = float(values[1])

            print(f"Gas Level: {gas_value}")
            print(f"Temperature: {temperature}")

            if gas_value > gas_threshold or temperature > temp_threshold:
                print("⚠ ALERT: Food quality may be decreasing!")
            else:
                print("Food condition is normal.")

        time.sleep(1)

    except:
        print("Error reading sensor data")
