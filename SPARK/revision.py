import requests
import pandas as pd
from pyspark.sql import SparkSession

def fetch_matches():
    url = "http://api.football-data.org/v2/competitions/CL/matches"
    headers = {"X-Auth-Token": "5efeea68fa60416cad757ca4d1cb0d79"}
    response = requests.get(url, headers=headers)
    matches = response.json()
    print("Respuesta completa de la API:", matches)  # Imprimir la respuesta completa para depuración
    return matches

# Obtener datos de la API
matches_data = fetch_matches()

# Verificar que la clave 'matches' está en el diccionario
if 'matches' in matches_data:
    matches_list = matches_data['matches']
    df = pd.json_normalize(matches_list)  # Convertir los datos a DataFrame de Pandas
    print(df.head())  # Imprimir las primeras filas para revisar
else:
    print("La clave 'matches' no se encuentra en los datos recibidos:", matches_data)
