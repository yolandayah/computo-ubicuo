import time

import requests
from colorama import Fore
from decouple import config

# ThingSpeak API parameters
API_KEY = config("API_KEY")
CHANNEL_ID = config("CHANNEL_ID")
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=10"


# Paso 1: Obtener los datos de ThingSpeak
def get_data_from_thingspeak(url):
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


# Paso 2: Procesar los datos recibidos y detectar anomalías
def process_data(feeds, last_entry_id):
    anomalies = []
    new_last_entry_id = last_entry_id

    for entry in feeds:
        entry_id = int(entry["entry_id"])
        if entry_id > last_entry_id:
            temperature = float(entry["field1"])
            humidity = float(entry["field2"])
            if temperature < 24 or temperature > 32:
                anomalies.append(
                    {
                        "type": "temperature",
                        "value": temperature,
                        "timestamp": entry["created_at"],
                    }
                )
            if humidity < 40 or humidity > 65:
                anomalies.append(
                    {
                        "type": "humidity",
                        "value": humidity,
                        "timestamp": entry["created_at"],
                    }
                )
            new_last_entry_id = max(new_last_entry_id, entry_id)

    return anomalies, new_last_entry_id


# Paso 3: Tomar acciones basadas en las anomalías detectadas
def take_action(anomalies):
    if anomalies:
        for anomaly in anomalies:
            if anomaly["type"] == "temperature":
                print(
                    f"{Fore.RED}Alerta: Temperatura anómala detectada con {anomaly['value']} °C en {anomaly['timestamp']}"
                )
            elif anomaly["type"] == "humidity":
                print(
                    f"{Fore.RED}Alerta: Humedad anómala detectada con {anomaly['value']}% en {anomaly['timestamp']}"
                )
    else:
        print(f"{Fore.WHITE}No se detectaron anomalías en la última actualización.")
    # Reset color
    # print(Style.RESET_ALL)


# Variable para guardar el ID de la última entrada procesada
last_entry_id = 0
# Ejecución del flujo con refresco cada 25 segundos
while True:
    data = get_data_from_thingspeak(url)
    if data:
        feeds = data["feeds"]
        anomalies, last_entry_id = process_data(feeds, last_entry_id)
        take_action(anomalies)
    time.sleep(20)
