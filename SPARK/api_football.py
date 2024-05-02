#5efeea68fa60416cad757ca4d1cb0d79

import requests
import pandas as pd
from pyspark.sql import SparkSession

def fetch_matches():
    url = "http://api.football-data.org/v2/competitions/CL/matches"
    headers = {"X-Auth-Token": "5efeea68fa60416cad757ca4d1cb0d79"}
    response = requests.get(url, headers=headers)
    matches = response.json()
    return matches

# Obtener los datos de los partidos
matches_data = fetch_matches()
matches_list = matches_data['matches']
df = pd.json_normalize(matches_list)

# Mostrar las primeras filas para verificar
print(df.head())

# Configuración de Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Football Data Analysis") \
    .getOrCreate()

# Convertir DataFrame de Pandas a DataFrame de Spark
matches_df = spark.createDataFrame(df)

# Mostrar las primeras filas del DataFrame de Spark para revisar
matches_df.show()

# Ejemplo de análisis: contar victorias de equipos locales
victorias_locales = matches_df.filter(matches_df['score.winner'] == "HOME_TEAM").count()
print(f"Número de victorias de equipos locales: {victorias_locales}")

# Finalizar la sesión de Spark
spark.stop()
