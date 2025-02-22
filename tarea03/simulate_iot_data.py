#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Simulando Datos de IoT
"""

import random
import time

import requests
from decouple import config


# Function to simulate sensor data
def simulate_sensor_data():
    # Simulate temperature between 20.0 and 30.0 degrees Celsius
    temperature = round(random.uniform(20.0, 30.0), 2)  # nosec B311
    # Simulate humidity between 30.0% and 70.0%
    humidity = round(random.uniform(30.0, 70.0), 2)  # nosec B311

    return temperature, humidity


# ThingSpeak API parameters
THINGSPEAK_API_KEY = config("THINGSPEAK_API_KEY")
THINGSPEAK_URL = "https://api.thingspeak.com/update"

while True:
    # Get simulated sensor data
    temperature, humidity = simulate_sensor_data()
    # Print simulated data
    print(f"Simulated Temp={temperature}*C Humidity={humidity}%")

    # Send data to ThingSpeak
    payload = {"api_key": THINGSPEAK_API_KEY, "field1": temperature, "field2": humidity}
    response = requests.post(THINGSPEAK_URL, data=payload, timeout=8)

    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully!")
    else:
        print("Failed to send data to ThingSpeak.")

    # Wait 10 seconds before next read
    time.sleep(10)
