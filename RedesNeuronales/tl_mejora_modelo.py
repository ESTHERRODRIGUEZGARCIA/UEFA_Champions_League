import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import class_weight
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Carga de datos
data_path = 'RedesNeuronales/combined_data.csv'
data = pd.read_csv(data_path)

# Normalización de los datos
scaler = MinMaxScaler()
features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
            'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion', 
            'Veces_Campeon', 'Veces_Subcampeon']
data[features] = scaler.fit_transform(data[features])

# Codificación de las etiquetas
data['equipo_encoded'] = pd.factorize(data['equipo'])[0]

# División de los datos
X_train, X_val, y_train, y_val = train_test_split(data[features], data['equipo_encoded'], test_size=0.2, random_state=42)

# Carga del modelo preentrenado y ajuste para nueva tarea
base_model = load_model('RedesNeuronales/modelo_entrenado.h5')
base_model.summary()

# Congelar todas las capas excepto las últimas dos
for layer in base_model.layers[:-2]:
    layer.trainable = False

new_model = Sequential(layers=base_model.layers[:-1])
new_model.add(Dense(len(np.unique(y_train)), activation='softmax', name='dense_output'))  # Nueva capa de salida con nombre único

new_model.compile(optimizer=Adam(learning_rate=1e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
history = new_model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_val, y_val)
)

# Evaluar el modelo
results = new_model.evaluate(X_val, y_val)
print(f"Loss: {results[0]}, Accuracy: {results[1]}")
