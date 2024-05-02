import pandas as pd
from data_fetcher import fetch_matches_from_api
from pyspark.sql import SparkSession


def create_spark_dataframe_from_api():
    # Obtener datos de la API
    matches_data = fetch_matches_from_api()
    
    # Convertir datos a un DataFrame de pandas
    pandas_df = pd.DataFrame(matches_data)
    
    # Iniciar SparkSession
    spark = SparkSession.builder \
        .appName("Football Data Analysis") \
        .getOrCreate()
    
    # Convertir DataFrame de pandas a DataFrame de Spark
    spark_df = spark.createDataFrame(pandas_df)
    
    return spark_df
