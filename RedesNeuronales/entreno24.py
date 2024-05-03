import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Cargar y preparar datos
combined_data = pd.read_csv('RedesNeuronales/combined_data.csv')
scaler = MinMaxScaler()
features_to_normalize = combined_data.columns[1:]  # Excluyendo la columna 'equipo'
combined_data_normalized = combined_data.copy()
combined_data_normalized[features_to_normalize] = scaler.fit_transform(combined_data[features_to_normalize])


X_full = np.concatenate([combined_data_normalized[features_to_normalize], combined_data_normalized[features_to_normalize]], axis=1)

label_encoder = LabelEncoder()
y_full_encoded = label_encoder.fit_transform(combined_data_normalized['equipo'])

# Definir la estructura de la red neuronal para aceptar 24 características
model = Sequential([
    Dense(128, activation='relu', input_shape=(24,)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(combined_data_normalized['equipo'].unique()), activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_full, y_full_encoded, epochs=100)

# Guardar el modelo entrenado
model.save('RedesNeuronales/modelo_entrenado_24_features.h5')
