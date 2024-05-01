import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Establecer estilo de los gráficos
sns.set(style="whitegrid")
#datos_semis_df = abrir csv: datos_gradio/datos_semis
datos_semis_df = pd.read_csv('semis/datos_semis.csv')

# Estadísticas descriptivas de los datos de semifinales
semis_stats = datos_semis_df.describe()

# Histograma de goles a favor
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, primer subplot
sns.histplot(datos_semis_df['media_goles_ataque'], kde=True, color='blue', binwidth=0.1)
plt.title('Distribución de Media de Goles de Ataque')

# Histograma de goles recibidos
plt.subplot(1, 2, 2)  # 1 fila, 2 columnas, segundo subplot
sns.histplot(datos_semis_df['goles_recibidos'], kde=True, color='red', binwidth=0.1)
plt.title('Distribución de Goles Recibidos')

plt.tight_layout()
plt.show()

semis_stats
