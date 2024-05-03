import pandas as pd
import os

global_temp_con_puntos_new = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')
resultados_octavos_new = pd.read_csv('datos_gradio/resultados_octavos.csv')
champions_league_new = pd.read_csv('datos_gradio/champions_league.csv')

# Filtrar datos de los equipos en semifinales en cada archivo relevante
equipos_semis = ['Real Madrid', 'Bayern Munich', 'Paris Saint-Germain', 'Borussia Dortmund']


datos_semis = pd.read_csv('datos_gradio/datos_semis.csv')

global_semis = global_temp_con_puntos_new[global_temp_con_puntos_new['equipo'].isin(equipos_semis)]

resultados_semis = resultados_octavos_new[resultados_octavos_new['Equipo'].isin(equipos_semis)]


champions_filtered = champions_league_new[
    (champions_league_new['campeon'].isin(equipos_semis)) | 
    (champions_league_new['subcampeon'].isin(equipos_semis))
]

champions_summary = champions_filtered.groupby('campeon').size().reindex(equipos_semis, fill_value=0)
subcampeon_summary = champions_filtered.groupby('subcampeon').size().reindex(equipos_semis, fill_value=0)


summary_stats = pd.DataFrame({
    'Veces_Campeon': champions_summary,
    'Veces_Subcampeon': subcampeon_summary
}).reset_index().rename(columns={'index': 'equipo'})

# Combinar estas estadísticas con 'datos_semis.csv'
combined_data = pd.merge(datos_semis, summary_stats, on='equipo', how='left')


