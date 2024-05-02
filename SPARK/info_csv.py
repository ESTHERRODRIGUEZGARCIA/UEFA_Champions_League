from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class SparkChampionsLeague:

    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("Analisis_Champions_Spark") \
            .getOrCreate()

    def stop(self):
        self.spark.stop()

    def read_file(self, path):
        return self.spark.read.csv(path, header=True, inferSchema=True)

    def create_temp_view(self, df, name):
        df.createOrReplaceTempView(name)

    def sql_query(self, query):
        return self.spark.sql(query).show()

    def predict(self, df):
        # Simulación de una función de predicción muy simple
        team_stats = df.groupBy('Squad').avg('Goals')
        team_stats.show()


if __name__ == "__main__":
    spark_app = SparkChampionsLeague()
    df = spark_app.read_file("datos_gradio/champions_league.csv")  # Cambia esto al path correcto
    spark_app.create_temp_view(df, "champions_data")
    spark_app.sql_query("SELECT * FROM champions_data LIMIT 10")  # Muestra los primeros 10 registros
    spark_app.predict(df)  # Ejemplo de función de predicción
    spark_app.stop()
