from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# Se lee el conjunto de datos del Real Madrid
real_madrid_data = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')

# Preparación de los datos de Real Madrid para análisis de estacionariedad
real_madrid_series = real_madrid_data.set_index('SEASON')['puntos']

# Test de Dickey-Fuller para verificar la estacionariedad
adf_test = adfuller(real_madrid_series)

# Mostrar los resultados del test
adf_results = {
    'Test Statistic': adf_test[0],
    'p-value': adf_test[1],
    'Lags Used': adf_test[2],
    'Number of Observations Used': adf_test[3],
    'Critical Values': adf_test[4],
}
print("ADF Test Results:", adf_results)

# Ajustando el modelo ARIMA a la serie temporal
model = ARIMA(real_madrid_series, order=(1, 0, 1))
model_fit = model.fit()

# Realizar predicciones
predictions = model_fit.forecast(steps=3)  # Prediciendo las próximas 3 temporadas

# Mostrar resumen del modelo y las predicciones
model_summary = model_fit.summary()
print(model_summary)
print("\nPredicted Points for Next 3 Seasons:")
for i, prediction in enumerate(predictions, 1):
    print(f"Season {i}: {prediction:.2f} points")
