import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import load_model

def probabilidad_semis():
    # Cargar el modelo entrenado
    model = load_model('RedesNeuronales/modelo_entrenado_24_features.h5')

    # Cargar y preparar los datos como se mostró previamente
    combined_data = pd.read_csv('RedesNeuronales/combined_data.csv')
    scaler = MinMaxScaler()
    features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
                'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion', 
                'Veces_Campeon', 'Veces_Subcampeon']
    combined_data[features] = scaler.fit_transform(combined_data[features])

    # Preparar los datos para los enfrentamientos
    teams_data = combined_data.set_index('equipo')
    rm_bm_data = np.concatenate((teams_data.loc['Real Madrid', features], teams_data.loc['Bayern Munich', features])).reshape(1, -1)
    psg_dortmund_data = np.concatenate((teams_data.loc['Paris Saint-Germain', features], teams_data.loc['Borussia Dortmund', features])).reshape(1, -1)

    # Hacer predicciones
    rm_bm_prob = model.predict(rm_bm_data)
    psg_dortmund_prob = model.predict(psg_dortmund_data)

    # Imprimir las probabilidades
    print("Probabilidades de victoria en el enfrentamiento Real Madrid vs Bayern Munich:")
    print(f"Real Madrid: {rm_bm_prob[0][0]*100:.2f}%")
    print(f"Bayern Munich: {rm_bm_prob[0][1]*100:.2f}%\n")

    print("Probabilidades de victoria en el enfrentamiento PSG vs Dortmund:")
    print(f"PSG: {psg_dortmund_prob[0][0]*100:.2f}%")
    print(f"Dortmund: {psg_dortmund_prob[0][1]*100:.2f}%")
