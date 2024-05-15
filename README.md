# UEFA_Champions_League


Click [aquí](https://github.com/ESTHERRODRIGUEZGARCIA/UEFA_Champions_League.git) para ver el enlace del repositorio.

Trabajo hecho por:
1. [Esther Rodríguez García](https://github.com/ESTHERRODRIGUEZGARCIA)


# INDICACIONES:
El archivo `main.py` sirve como punto central para la ejecución de varios módulos de análisis de datos y modelos predictivos relacionados con la UEFA Champions League. Mediante un menú interactivo, el usuario puede seleccionar y ejecutar diferentes tipos de análisis y visualizaciones. Las opciones incluyen: un modelo de regresión lineal que estima las probabilidades de ganar la Champions League 2023-2024 desde los octavos de final; un análisis avanzado de regresión lineal para predecir el ganador final; predicciones basadas en redes neuronales; modelos de árbol de decisión y bosque aleatorio para análisis predictivo, junto con sus visualizaciones correspondientes; análisis de datos de series temporales utilizando modelos ARIMA; y la generación de gráficas y estadísticas detalladas de los equipos semifinalistas. Además, se incluyen intentos de realizar análisis avanzados con LangChain y Llama 3, así como con Spark, aunque estos no se han implementado con éxito. El programa permite la ejecución continua de múltiples análisis hasta que el usuario decida finalizar.

## Parte de Regresión Lineal
En este repositorio, se lleva a cabo una refinación de la información obtenida en la entrega previa de análisis de datos, con el propósito de mejorar su calidad y relevancia. Este proceso implica una revisión exhaustiva de los datos previamente recopilados, así como la incorporación de nuevas métricas y técnicas analíticas para obtener una comprensión más profunda y precisa del panorama actual.

Una vez completada la fase de refinación de datos, se procede a realizar una regresión lineal utilizando las variables relevantes identificadas en el análisis anterior. Esta regresión proporcionará un modelo predictivo que permitirá estimar las posibilidades de éxito de los equipos participantes en la Champions League de la temporada actual.

Finalmente, se genera un ranking de los equipos basado en las predicciones obtenidas mediante el modelo de regresión lineal. Este ranking ofrece una visión ordenada de los equipos que se considera que tienen mayores probabilidades de ganar la Champions League en la temporada en curso.

Resultado final de la regresión lineal:

![resultado_estudio_UCL](https://github.com/ESTHERRODRIGUEZGARCIA/UEFA_Champions_League/assets/91721860/bede766e-77d1-4d7f-9199-4905026ede01)



# Modelo de árbol de decisión y bosques aleatorios: 

- Objetivo del modelo: predecir el ganador de las semifinales de la UEFA Champions League y, finalmente, predecir el campeón del torneo. Utiliza un modelo de bosque aleatorio para estimar las probabilidades de que cada equipo tenga una alta probabilidad de ganar basándose en varias estadísticas y rendimientos históricos.

### Datos Utilizados
El modelo utiliza dos conjuntos principales de datos:

El archivo `datos_semis.csv` contiene estadísticas actuales de los equipos que compiten en las semifinales, incluyendo la media de goles de ataque, tiros a puerta, penaltis a favor, córners, faltas recibidas, fuera de juego, goles recibidos, tiros a puerta recibidos, penaltis en contra y posesión. Además, se ha añadido una variable objetivo llamada `alta_probabilidad_ganar`, la cual señala si un equipo tiene una alta probabilidad de ganar, considerando una posesión igual o superior al 50% y una media de goles de ataque mayor a 1.75. Por otro lado, el archivo `global_temp_con_puntos.csv` proporciona el rendimiento histórico de los equipos durante las últimas dos temporadas, detallando el número de partidos jugados, ganados, empatados y perdidos, así como los goles a favor, en contra y los puntos acumulados.
Estos datos se agregan para cada equipo y se combinan con las estadísticas de las semifinales para formar un conjunto de datos más completo.

### Preparación y Limpieza de Datos
- Los datos de ambos archivos se combinan usando el nombre del equipo como clave.
- Se manejan los valores faltantes utilizando imputación por la media, lo que significa que cualquier dato faltante se reemplaza por el promedio de su columna respectiva.

### Modelado
- Se divide el conjunto de datos combinado en entrenamiento y prueba (50% cada uno, debido al pequeño tamaño de los datos).
- Se entrenan dos modelos: un **Árbol de Decisión** y un **Bosque Aleatorio**. El árbol de decisión es útil para entender la importancia de las características y cómo las decisiones están siendo tomadas, mientras que el bosque aleatorio, que es un conjunto de muchos árboles de decisión, es generalmente más robusto y mejor para estimar probabilidades.
- Se evalúan los modelos basándose en su precisión, y se usa el bosque aleatorio para predecir las probabilidades de ganar para cada equipo.

### Simulación de Enfrentamientos
- Utilizando las probabilidades predichas por el bosque aleatorio, se simulan los enfrentamientos entre los equipos de las semifinales: Real Madrid vs Bayern Munich y PSG vs Borussia Dortmund.
- Los ganadores de cada enfrentamiento se determinan comparando las probabilidades de ganar.
- Finalmente, se simula un enfrentamiento entre los dos ganadores de las semifinales para determinar el campeón del torneo.

Este modelo intenta aprovechar tanto el rendimiento actual como el histórico para hacer predicciones informadas sobre los resultados de los partidos, considerando una amplia gama de factores que pueden influir en el desempeño del equipo.

# Modelo predictivo basado en redes neuronales: 
Preprocesamiento de Datos:

- Normalización: Los datos numéricos fueron normalizados usando MinMaxScaler para asegurar que todas las características tengan el mismo peso durante el entrenamiento del modelo.
- Etiquetado: Se utilizó LabelEncoder para transformar las etiquetas categóricas de los nombres de los equipos en valores numéricos que el modelo puede procesar.
  
### Modelo Predictivo
Se desarrolló una red neuronal utilizando TensorFlow y Keras con la siguiente arquitectura:

- Capa de entrada: Recibe las características normalizadas de los equipos.
- Capas ocultas: Dos capas densas con 128 y 64 neuronas respectivamente, cada una seguida de una capa de abandono (Dropout) para reducir el sobreajuste.
- Capa de salida: Una capa densa con una función de activación softmax, que proporciona las probabilidades de que cada equipo sea el ganador.
### Entrenamiento del Modelo
El modelo se entrenó con los datos combinados y normalizados de todos los equipos participantes, utilizando una función de pérdida de entropía cruzada y el optimizador Adam. Se llevó a cabo durante 100 épocas para permitir una convergencia adecuada del modelo.

### Evaluación y Uso del Modelo
El modelo se evaluó en términos de precisión durante el entrenamiento, mostrando cómo aprendía a clasificar correctamente entre los equipos. Para hacer predicciones, se prepararon los datos de los enfrentamientos específicos (e.g., Real Madrid vs. Bayern Munich), combinando las características de los dos equipos involucrados en cada partido. El modelo entonces predice las probabilidades de cada equipo para ganar el enfrentamiento.

### Resultados y Observaciones
El modelo demostró fluctuaciones en la precisión durante las primeras épocas de entrenamiento pero se estabilizó a medida que continuaba el proceso de entrenamiento. Las predicciones realizadas reflejan las probabilidades de cada equipo para ganar según las características presentadas, ofreciendo una herramienta útil para análisis predictivo en el contexto deportivo. Este modelo de red neuronal ofrece un enfoque sistemático y basado en datos para predecir los resultados de partidos de fútbol en un torneo de alta importancia. Con adecuadas mejoras y ajustes, podría extenderse para otras aplicaciones en análisis deportivo o adaptarse a diferentes conjuntos de datos y escenarios competitivos.


