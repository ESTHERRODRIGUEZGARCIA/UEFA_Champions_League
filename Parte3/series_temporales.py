#analizar una serie temporal de puntos acumulados por temporada
#1. Real Madrid

import matplotlib.pyplot as plt
import pandas as pd


data_global_temp = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')

real_madrid_data = data_global_temp[data_global_temp['equipo'] == 'Real Madrid']

real_madrid_data = real_madrid_data.sort_values('SEASON')

plt.figure(figsize=(10, 5))
plt.plot(real_madrid_data['SEASON'], real_madrid_data['puntos'], marker='o', linestyle='-', color='blue')
plt.title('Puntos Acumulados por Temporada - Real Madrid')
plt.xlabel('Temporada')
plt.ylabel('Puntos')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# 2. Paris Saint-Germain
psg_data = data_global_temp[data_global_temp['equipo'] == 'Paris Saint-Germain']

psg_data = psg_data.sort_values('SEASON')

plt.figure(figsize=(10, 5))
plt.plot(psg_data['SEASON'], psg_data['puntos'], marker='o', linestyle='-', color='red')
plt.title('Puntos Acumulados por Temporada - Paris Saint-Germain')
plt.xlabel('Temporada')
plt.ylabel('Puntos')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# 3. Borussia Dortmund
dortmund_data = data_global_temp[data_global_temp['equipo'] == 'Borussia Dortmund']

dortmund_data = dortmund_data.sort_values('SEASON')

plt.figure(figsize=(10, 5))
plt.plot(dortmund_data['SEASON'], dortmund_data['puntos'], marker='o', linestyle='-', color='yellow')
plt.title('Puntos Acumulados por Temporada - Borussia Dortmund')
plt.xlabel('Temporada')
plt.ylabel('Puntos')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
