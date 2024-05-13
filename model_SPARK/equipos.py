from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, MapType
from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Ejemplo de lectura de JSON") \
    .getOrCreate()

# Definir el esquema del archivo JSON
schema = StructType([
    StructField("Real Madrid", StructType([
        StructField("count", IntegerType(), True),
        StructField("filters", MapType(StringType(), StringType()), True),
        StructField("matches", ArrayType(
            StructType([
                StructField("id", StringType(), True),
                StructField("utcDate", StringType(), True),
                StructField("status", StringType(), True),
                StructField("matchday", StringType(), True),
                StructField("score", StructType([
                    StructField("winner", StringType(), True),
                    StructField("fullTime", StructType([
                        StructField("homeTeam", IntegerType(), True),
                        StructField("awayTeam", IntegerType(), True)
                    ]), True)
                ]), True),
                StructField("homeTeam", StructType([
                    StructField("name", StringType(), True)
                ]), True),
                StructField("awayTeam", StructType([
                    StructField("name", StringType(), True)
                ]), True),
            ])
        ), True)
    ]), True),
])

# Leer el JSON con el esquema definido
df = spark.read.schema(schema).json("SPARK/team_matches.json")

# Mostrar el esquema del DataFrame
df.printSchema()

# Mostrar los primeros 5 registros del DataFrame sin truncar las columnas
df.show(5, truncate=False)
