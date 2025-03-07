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
        "divice_id": [],
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


def main():
    """
    Comentario de la función
    """
    print("Hola Mundo")


if __name__ == "__main__":
    main()
