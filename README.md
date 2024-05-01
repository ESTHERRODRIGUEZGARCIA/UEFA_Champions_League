# UEFA_Champions_League


Click [aquí](https://github.com/ESTHERRODRIGUEZGARCIA/UEFA_Champions_League.git) para ver el enlace del repositorio.

Trabajo hecho por:
1. [Esther Rodríguez García](https://github.com/ESTHERRODRIGUEZGARCIA)

En este repositorio, se lleva a cabo una refinación de la información obtenida en la entrega previa de análisis de datos, con el propósito de mejorar su calidad y relevancia. Este proceso implica una revisión exhaustiva de los datos previamente recopilados, así como la incorporación de nuevas métricas y técnicas analíticas para obtener una comprensión más profunda y precisa del panorama actual.

Una vez completada la fase de refinación de datos, se procede a realizar una regresión lineal utilizando las variables relevantes identificadas en el análisis anterior. Esta regresión proporcionará un modelo predictivo que permitirá estimar las posibilidades de éxito de los equipos participantes en la Champions League de la temporada actual.

Finalmente, se genera un ranking de los equipos basado en las predicciones obtenidas mediante el modelo de regresión lineal. Este ranking ofrece una visión ordenada de los equipos que se considera que tienen mayores probabilidades de ganar la Champions League en la temporada en curso.

Resultado final de la regresión lineal:

![resultado_estudio_UCL](https://github.com/ESTHERRODRIGUEZGARCIA/UEFA_Champions_League/assets/91721860/bede766e-77d1-4d7f-9199-4905026ede01)



## Modelo de árbol de decisión y bosques aleatorios: 

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
