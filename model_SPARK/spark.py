from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc, explode

# Inicializar la sesión de Spark
spark = SparkSession.builder \
    .appName("ApuestasAnalysis") \
    .getOrCreate()

# Definir el esquema esperado para los datos
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, MapType

schema = StructType([
    StructField("Real Madrid", StructType([
        StructField("count", IntegerType(), True),
        StructField("filters", StructType([
            StructField("permission", StringType(), True),
            StructField("limit", IntegerType(), True)
        ]), True),
        StructField("matches", ArrayType(StructType([
            StructField("id", IntegerType(), True),
            StructField("competition", StructType([
                StructField("id", IntegerType(), True),
                StructField("name", StringType(), True),
                StructField("area", StructType([
                    StructField("name", StringType(), True),
                    StructField("code", StringType(), True),
                    StructField("ensignUrl", StringType(), True)
                ]), True)
            ]), True),
            StructField("season", StructType([
                StructField("id", IntegerType(), True),
                StructField("startDate", StringType(), True),
                StructField("endDate", StringType(), True),
                StructField("currentMatchday", IntegerType(), True),
                StructField("winner", StringType(), True)
            ]), True),
            StructField("utcDate", StringType(), True),
            StructField("status", StringType(), True),
            StructField("matchday", IntegerType(), True),
            StructField("stage", StringType(), True),
            StructField("group", StringType(), True),
            StructField("lastUpdated", StringType(), True),
            StructField("odds", MapType(StringType(), StringType()), True),
            StructField("score", StructType([
                StructField("winner", StringType(), True),
                StructField("duration", StringType(), True),
                StructField("fullTime", StructType([
                    StructField("homeTeam", IntegerType(), True),
                    StructField("awayTeam", IntegerType(), True)
                ]), True),
                StructField("halfTime", StructType([
                    StructField("homeTeam", IntegerType(), True),
                    StructField("awayTeam", IntegerType(), True)
                ]), True),
                StructField("extraTime", StructType([
                    StructField("homeTeam", IntegerType(), True),
                    StructField("awayTeam", IntegerType(), True)
                ]), True),
                StructField("penalties", StructType([
                    StructField("homeTeam", IntegerType(), True),
                    StructField("awayTeam", IntegerType(), True)
                ]), True)
            ]), True),
            StructField("homeTeam", StructType([
                StructField("id", IntegerType(), True),
                StructField("name", StringType(), True)
            ]), True),
            StructField("awayTeam", StructType([
                StructField("id", IntegerType(), True),
                StructField("name", StringType(), True)
            ]), True),
            StructField("referees", ArrayType(StructType([
                StructField("id", IntegerType(), True),
                StructField("name", StringType(), True),
                StructField("role", StringType(), True),
                StructField("nationality", StringType(), True)
            ])), True)
        ])), True)
    ]), True)
])

# Cargar el archivo JSON en un DataFrame de Spark
raw_df = spark.read.schema(schema).json("model_SPARK/team_matches.json")

# Filtrar registros corruptos
corrupt_records = raw_df.filter(col("_corrupt_record").isNotNull())
corrupt_records.show(truncate=False)

# Filtrar y mostrar registros válidos
valid_records = raw_df.filter(col("_corrupt_record").isNull())
valid_records.show(truncate=False)

# Seleccionar las columnas relevantes y expandir la estructura anidada
matches_df = valid_records.select(explode("Real Madrid.matches").alias("match"))

# Expandir las columnas anidadas dentro de cada equipo
matches_df = matches_df.selectExpr(
    "match.id", 
    "match.competition.name as competition_name", 
    "match.season.startDate as season_start", 
    "match.season.endDate as season_end",
    "match.utcDate as match_date", 
    "match.status", 
    "match.matchday",
    "match.stage", 
    "match.score.winner", 
    "match.score.fullTime.homeTeam as home_score",
    "match.score.fullTime.awayTeam as away_score",
    "match.homeTeam.name as home_team", 
    "match.awayTeam.name as away_team"
)

# Mostrar los datos limpios
matches_df.show(truncate=False)

# Análisis Exploratorio de Datos
# Contar el número de partidos por equipo local
home_team_counts = matches_df.groupBy("home_team").agg(count("id").alias("home_matches")).orderBy(desc("home_matches"))

# Contar el número de partidos por equipo visitante
away_team_counts = matches_df.groupBy("away_team").agg(count("id").alias("away_matches")).orderBy(desc("away_matches"))

# Mostrar los equipos con más partidos como local y visitante
home_team_counts.show()
away_team_counts.show()

# Procesamiento en Tiempo Real (simulación)
# Supongamos que los datos en tiempo real se encuentran en el directorio /mnt/data/streaming_team_matches/

streaming_df = spark.readStream \
    .schema(matches_df.schema) \
    .json("/mnt/data/streaming_team_matches/")

# Función para procesar datos entrantes
def process_incoming_data(df, epoch_id):
    # Realizar operaciones en el DataFrame
    df.groupBy("home_team").agg(count("id").alias("match_count")).show()

# Iniciar el flujo de procesamiento
query = streaming_df.writeStream \
    .foreachBatch(process_incoming_data) \
    .start()

query.awaitTermination()

# Modelado Estadístico y Machine Learning
# Preparar los datos para el modelo
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

feature_cols = ["home_score", "away_score"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
matches_df = assembler.transform(matches_df)

# Entrenar un modelo de regresión lineal
lr = LinearRegression(featuresCol="features", labelCol="winner")
lr_model = lr.fit(matches_df)

# Mostrar los coeficientes del modelo
print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")

# Visualización de Datos
# Convertir DataFrame de Spark a Pandas para visualización
pandas_df = matches_df.toPandas()

import matplotlib.pyplot as plt

# Crear un gráfico de barras del número de partidos por equipo local
pandas_df['home_team'].value_counts().plot(kind='bar')
plt.xlabel('Home Team')
plt.ylabel('Number of Matches')
plt.title('Number of Matches by Home Team')
plt.show()
