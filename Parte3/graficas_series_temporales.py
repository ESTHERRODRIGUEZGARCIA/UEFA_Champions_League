from pmdarima import auto_arima
import pandas as pd

# Se lee el conjunto de datos del Real Madrid
real_madrid_data = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')
real_madrid_series = real_madrid_data.set_index('SEASON')['puntos']

# Uso de auto_arima para encontrar el mejor modelo ARIMA automáticamente
auto_model = auto_arima(real_madrid_series, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)

# Imprimir el resumen del mejor modelo
print(auto_model.summary())

# Predecir las próximas 3 temporadas
predictions = auto_model.predict(n_periods=3)
print("\nPredicted Points for Next 3 Seasons:")
for i, prediction in enumerate(predictions, 1):
    print(f"Season {i}: {prediction:.2f} points")
