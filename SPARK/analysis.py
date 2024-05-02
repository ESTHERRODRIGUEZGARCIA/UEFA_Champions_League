from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from spark_session import start_spark_session
from data_processing import create_dataframe

def run_analysis():
    # Iniciar sesión de Spark
    spark = start_spark_session()
    
    # Crear DataFrame
    df = create_dataframe()
    
    if not df.empty:
        # Convertir DataFrame de pandas a DataFrame de Spark
        matches_df = spark.createDataFrame(df)
        
        # Indexar equipos
        teamIndexer = StringIndexer(inputCol="TeamName", outputCol="indexedTeam")
        
        # Vector de características
        assembler = VectorAssembler(inputCols=["indexedTeam", "GoalsFor", "GoalsAgainst"], outputCol="features")
        
        # Dividir datos en conjuntos de entrenamiento y prueba
        (trainingData, testData) = matches_df.randomSplit([0.8, 0.2])
        
        # Definir el modelo RandomForest
        rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)
        
        # Construir el pipeline
        pipeline = Pipeline(stages=[teamIndexer, assembler, rf])
        
        # Entrenar el modelo
        model = pipeline.fit(trainingData)
        
        # Predicciones
        predictions = model.transform(testData)
        
        # Evaluación
        evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
        accuracy = evaluator.evaluate(predictions)
        print("Test Accuracy = %g" % (accuracy))
        
        # Mostrar resultados
        predictions.select("TeamName", "prediction").show()
        
        print("Análisis completado.")
    else:
        print("DataFrame vacío, no se realiza el análisis.")
