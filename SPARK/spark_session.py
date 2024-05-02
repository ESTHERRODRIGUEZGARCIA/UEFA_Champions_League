from pyspark.sql import SparkSession

def start_spark_session(app_name="Football Data Analysis"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark