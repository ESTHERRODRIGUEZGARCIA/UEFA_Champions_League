from sklearn.utils import class_weight
import numpy as np
from tl_modelo import y_train

# Calcula los pesos de las clases basados en la frecuencia de las clases
class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights_dict = dict(enumerate(class_weights))

print("Pesos de las clases:", class_weights_dict)


# Verificar valores únicos y sus correspondientes pesos
unique_classes = np.unique(y_train)
print("Clases únicas:", unique_classes)
print("Pesos de clases calculados:", class_weights_dict)

# Ajustar el modelo si es necesario
# Por ejemplo, modificar la capa de salida si las clases no están bien representadas
