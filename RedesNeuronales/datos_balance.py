from sklearn.utils import class_weight
import numpy as np
from modelo_transfer_learning import y_train

# Calcula los pesos de las clases basados en la frecuencia de las clases
class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights_dict = dict(enumerate(class_weights))

print("Pesos de las clases:", class_weights_dict)
