#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tarea 5 de computo ubicuo
"""

import random
import time

import pandas as pd


def edge_device(device_id):
    """
    Simulación de dispositivos IoT que generan datos
    """
    data = {
        "timestamp": [],
        "device_id": [],
        "temperature": [],
        "humidity": [],
    }

    # Simulación de 10 lecturas de sensor
    for _ in range(10):
        timestamp = time.time()
        temperature = random.uniform(20.0, 30.0)  # nosec B311 blacklist
        humidity = random.uniform(30.0, 70.0)  # nosec B311 blacklist
        data["timestamp"].append(timestamp)
        data["device_id"].append(device_id)
        data["temperature"].append(temperature)
        data["humidity"].append(humidity)
        # Espera de 1 segundo entre lecturas
        time.sleep(1)

    return pd.DataFrame(data)


def fog_node(device_data_list):
    """
    Simulación de Fog Computing: Agregación de datos múltiples dispositivos
    """
    aggregated_data = pd.concat(device_data_list)
    aggregated_data["avg_temperature"] = aggregated_data["temperature"].mean()
    aggregated_data["avg_humidity"] = aggregated_data["humidity"].mean()

    return aggregated_data


def roof_node(fog_data_list):
    """
    Simulación de Roff Computing: Coordinación y optimización de recursos
    """
    roof_data = pd.concat(fog_data_list)
    roof_data["overall_avg_temperature"] = roof_data["avg_temperature"].mean()
    roof_data["overall_avg_humidity"] = roof_data["avg_humidity"].mean()

    return roof_data


def cloud_processing(roof_data):
    """
    Simulación de Cloud Computing: Almacenamiento y procesamiento avanzado
    """
    # Aquí podrías agregar procesamiento avanzado, almacenameinto en la nube,
    # etc.
    print("Datos procesados en la nube:")
    print(roof_data)


def main_simulation():
    """
    Función principal para la simulación
    """
    # Simulación de Edge Computing
    edge_data_list = []

    # Simulación de 5 dispositivos IoT
    for i in range(5):
        edge_data_list.append(edge_device(f"device_{i + 1}"))

    # Simulación de Fog Computing
    fog_data = fog_node(edge_data_list)

    # Simulación de Roof Computing
    roof_data = roof_node([fog_data])

    # Simulación de Cloud Computing
    cloud_processing(roof_data)


if __name__ == "__main__":
    main_simulation()
