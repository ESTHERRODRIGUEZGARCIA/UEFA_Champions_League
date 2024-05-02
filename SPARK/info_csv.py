import pandas as pd
from pyspark.sql import SparkSession

def create_dataframe_from_csv():
    # Ruta al archivo CSV
    file_path = "datos_gradio/datos_semis.csv"
    
    # Leer el archivo CSV y crear un DataFrame de pandas
    df = pd.read_csv(file_path)
    
    return df


def create_spark_dataframe_from_csv():
    # Iniciar SparkSession
    spark = SparkSession.builder \
        .appName("Football Data Analysis") \
        .getOrCreate()
    
    # Crear DataFrame de pandas desde CSV
    pandas_df = create_dataframe_from_csv()
    
    # Convertir DataFrame de pandas a DataFrame de Spark
    spark_df = spark.createDataFrame(pandas_df)
    
    return spark_df

def main():
    # Crear DataFrame de Spark
    spark_df = create_spark_dataframe_from_csv()
    
    # Mostrar esquema del DataFrame
    spark_df.printSchema()
    
    # Mostrar los primeros registros del DataFrame
    spark_df.show()


if __name__ == "__main__":
    main()
    