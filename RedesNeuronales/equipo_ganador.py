import numpy as np
from entreno import *

# Hacer predicciones
predictions = model.predict(X_full)
predicted_classes = np.argmax(predictions, axis=1)
predicted_teams = label_encoder.inverse_transform(predicted_classes)

# Imprimir las predicciones con sus respectivas probabilidades
for i, team in enumerate(predicted_teams):
    print(f"Equipo: {team}, Probabilidad: {np.max(predictions[i])*100:.2f}%")
