from pyspark.sql import SparkSession
import json

# Inicializar la sesión de Spark
spark = SparkSession.builder \
    .appName("ApuestasAnalysis") \
    .getOrCreate()

# Leer el JSON con el esquema definido
df = spark.read.json("model_SPARK/team_matches.json")

# Mostrar el esquema del DataFrame
df.printSchema()

# Seleccionar columnas relevantes y renombrar si es necesario
matches_df = df.selectExpr("explode(matches) as match")

# Expandir las columnas anidadas
matches_df = matches_df.selectExpr("match.id", "match.competition.name as competition_name", 
                                   "match.season.startDate as season_start", "match.season.endDate as season_end",
                                   "match.utcDate as match_date", "match.status", "match.matchday",
                                   "match.stage", "match.score.winner", "match.score.fullTime.homeTeam as home_score",
                                   "match.score.fullTime.awayTeam as away_score",
                                   "match.homeTeam.name as home_team", "match.awayTeam.name as away_team")

# Mostrar los datos limpios
matches_df.show()

