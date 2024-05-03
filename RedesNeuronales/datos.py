import pandas as pd
import os

# Leer los archivos relevantes y almacenarlos en DataFrames
global_temp_con_puntos_new = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')
resultados_octavos_new = pd.read_csv('datos_gradio/resultados_octavos.csv')
champions_league_new = pd.read_csv('datos_gradio/champions_league.csv')

# Filtrar datos de los equipos en semifinales en cada archivo relevante
equipos_semis = ['Real Madrid', 'Bayern Munich', 'Paris Saint-Germain', 'Borussia Dortmund']

# Leer el archivo 'datos_semis.csv'
datos_semis = pd.read_csv('datos_gradio/datos_semis.csv')

# Filtrar datos en 'global_temp_con_puntos.csv'
global_semis = global_temp_con_puntos_new[global_temp_con_puntos_new['equipo'].isin(equipos_semis)]

# Filtrar datos en 'resultados_octavos.csv'
resultados_semis = resultados_octavos_new[resultados_octavos_new['Equipo'].isin(equipos_semis)]

# Filtrar datos en 'champions_league.csv' para estos equipos
# Dado que 'champions_league.csv' lista campeones y subcampeones, lo manejaremos un poco diferente
champions_filtered = champions_league_new[
    (champions_league_new['campeon'].isin(equipos_semis)) | 
    (champions_league_new['subcampeon'].isin(equipos_semis))
]

# Un ejemplo simple de combinación sería agregar datos como el número de veces campeón o subcampeón
champions_summary = champions_filtered.groupby('campeon').size().reindex(equipos_semis, fill_value=0)
subcampeon_summary = champions_filtered.groupby('subcampeon').size().reindex(equipos_semis, fill_value=0)

# Crear un nuevo DataFrame combinando estas estadísticas
# Asumiendo que el índice es el nombre del equipo
summary_stats = pd.DataFrame({
    'Veces_Campeon': champions_summary,
    'Veces_Subcampeon': subcampeon_summary
}).reset_index().rename(columns={'index': 'equipo'})

# Combinar estas estadísticas con 'datos_semis.csv'
combined_data = pd.merge(datos_semis, summary_stats, on='equipo', how='left')


