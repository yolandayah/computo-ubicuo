import random
import time

import requests
from decouple import config

# ThingSpeak API parameters
API_KEY = config("API_KEY")
BASE_URL = config("BASE_URL")


def data_send(temperatura, humedad):  # Funcion para mandar datos a ThingSpeak
    payload = {"api_key": API_KEY, "field1": temperatura, "field2": humedad}
    response = requests.get(BASE_URL, params=payload, timeout=5)
    if response.status_code == 200:
        print("Datos enviados a ThinSpeak correctamente!")
    else:
        print(f"Algo se rompió: {response.status_code}")


while True:
    temp = random.uniform(20.0, 38.0)  # nosec B311
    humidity = random.uniform(30.0, 80.0)  # nosec B311
    print(f"Sending temperature: {temp:.2f}, Humidity: {humidity:.2f}")
    data_send(temp, humidity)
    time.sleep(20)  # Wait 20 seg
