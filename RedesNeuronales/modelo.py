import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf

# Cargar datos
datos_semis = pd.read_csv('datos_gradio/datos_semis.csv')

# Seleccionar características y etiqueta
features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
            'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion']
X = datos_semis[features]
y = datos_semis['equipo']

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Preparar las etiquetas para la clasificación
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Ajustar y transformar y completo

# División de los datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.25, random_state=42)

# Definir la estructura de la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(y.unique()), activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))
