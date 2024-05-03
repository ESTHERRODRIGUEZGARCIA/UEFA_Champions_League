from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

from tl_mejora_datos import X_train, y_train

# Define un modelo más simple
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],), name='dense_1'),
    Dropout(0.5, name='dropout_1'),
    Dense(16, activation='relu', name='dense_2'),
    Dropout(0.3, name='dropout_2'),
    Dense(len(np.unique(y_train)), activation='softmax', name='output')
])


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
