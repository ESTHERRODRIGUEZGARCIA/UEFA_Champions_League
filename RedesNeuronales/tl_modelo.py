from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tl_datos import X_train, X_val, y_train, y_val, label_encoder

# Cargar el modelo preentrenado
model = load_model('RedesNeuronales/modelo_entrenado.h5')

# Congelar las capas excepto las últimas
for layer in model.layers[:-2]:
    layer.trainable = False

# Modificar la capa de salida para la nueva tarea
model.pop()  # Elimina la última capa

# Agregar nuevas capas con nombres únicos
model.add(Dense(64, activation='relu', name='dense_transfer_1'))
model.add(Dropout(0.5, name='dropout_transfer_1'))
model.add(Dense(len(label_encoder.classes_), activation='softmax', name='output_transfer'))

# Compilar el modelo modificado
model.compile(optimizer=Adam(learning_rate=1e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo modificado en tus datos
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_val, y_val))
