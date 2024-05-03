import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import class_weight
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

data_path = 'RedesNeuronales/combined_data.csv'
data = pd.read_csv(data_path)

# Normalizamos
scaler = MinMaxScaler()
features = ['media_goles_ataque', 'tiros_puerta', 'penaltis_favor', 'corners', 'faltas_recibidas', 
            'fuera_juego', 'goles_recibidos', 'tiros_puerta_recibidos', 'penalti_contra', 'posesion', 
            'Veces_Campeon', 'Veces_Subcampeon']
data[features] = scaler.fit_transform(data[features])

# etiquetas para la clasificación
data['equipo_encoded'] = pd.factorize(data['equipo'])[0]

# Dividimos los datos:entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(data[features], data['equipo_encoded'], test_size=0.2, random_state=42)

# Calcula los pesos de las clases basados en la frecuencia de las clases
class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights_dict = dict(enumerate(class_weights))

#modelo más simple porque el otro nos da resultados inválidos
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(16, activation='relu'),
    Dropout(0.3),
    Dense(len(np.unique(y_train)), activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=1e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Entrenamieneto  del modelo
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_val, y_val),
    class_weight=class_weights_dict  # Usa los pesos de clase si los datos están desbalanceados
)

# Evaluar el modelo
results = model.evaluate(X_val, y_val)
print(f"Loss: {results[0]}, Accuracy: {results[1]}")


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy over Epochs')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over Epochs')
plt.legend()

plt.show()
