import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import tensorflow as tf
from entreno import *

# Cargar los datos
combined_data = pd.read_csv('RedesNeuronales/combined_data.csv')

# Normalizar las características
scaler = MinMaxScaler()
features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
            'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion', 
            'Veces_Campeon', 'Veces_Subcampeon']
combined_data[features] = scaler.fit_transform(combined_data[features])

# Preparar los datos para los enfrentamientos directos
teams_data = combined_data.set_index('equipo')

# Concatenar datos para Real Madrid vs. Bayern Munich y PSG vs. Dortmund
rm_bm_data = np.concatenate((teams_data.loc['Real Madrid', features], teams_data.loc['Bayern Munich', features])).reshape(1, -1)
psg_dortmund_data = np.concatenate((teams_data.loc['Paris Saint-Germain', features], teams_data.loc['Borussia Dortmund', features])).reshape(1, -1)

# Cargar modelo y hacer predicciones
model = load_model()  # Asumimos que existe una función para cargar el modelo
rm_bm_prob = model.predict(rm_bm_data)
psg_dortmund_prob = model.predict(psg_dortmund_data)

# Suponemos que label_encoder está ajustado para interpretar las clases correctamente
label_encoder = LabelEncoder()
label_encoder.classes_ = np.array(['Real Madrid', 'Bayern Munich', 'Paris Saint-Germain', 'Borussia Dortmund'])

# Imprimir las probabilidades
print("Probabilidades de victoria en el enfrentamiento Real Madrid vs Bayern Munich:")
print(f"Real Madrid: {rm_bm_prob[0][0]*100:.2f}%")
print(f"Bayern Munich: {rm_bm_prob[0][1]*100:.2f}%\n")

print("Probabilidades de victoria en el enfrentamiento PSG vs Dortmund:")
print(f"PSG: {psg_dortmund_prob[0][0]*100:.2f}%")
print(f"Dortmund: {psg_dortmund_prob[0][1]*100:.2f}%")
