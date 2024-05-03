import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

combined_data = pd.read_csv('RedesNeuronales/combined_data.csv')
# Normalizar los datos
scaler = MinMaxScaler()
features_to_normalize = combined_data.columns[1:]  # Excluyendo la columna 'equipo'
combined_data_normalized = combined_data.copy()
combined_data_normalized[features_to_normalize] = scaler.fit_transform(combined_data[features_to_normalize])

# Preparar las etiquetas para la clasificación
label_encoder = LabelEncoder()
y_full_encoded = label_encoder.fit_transform(combined_data_normalized['equipo'])
X_full = combined_data_normalized[features_to_normalize]

# Definir la estructura de la red neuronal
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_full.shape[1],)),
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
history = model.fit(X_full, y_full_encoded, epochs=100)  # Usando todos los datos para entrenamiento

# Mostrar la estructura del modelo
model.summary()
