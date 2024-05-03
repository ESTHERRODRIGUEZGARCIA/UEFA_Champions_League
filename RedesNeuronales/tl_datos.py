import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# Cargar datos
data_path = 'RedesNeuronales/combined_data.csv'
data = pd.read_csv(data_path)

# Normalizar las características
scaler = MinMaxScaler()
features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
            'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion', 
            'Veces_Campeon', 'Veces_Subcampeon']
data[features] = scaler.fit_transform(data[features])

# Preparar las etiquetas para la clasificación
label_encoder = LabelEncoder()
data['equipo_encoded'] = label_encoder.fit_transform(data['equipo'])

# Dividir los datos en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(data[features], data['equipo_encoded'], test_size=0.2, random_state=42)
