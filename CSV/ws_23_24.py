import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://fbref.com/es/comps/8/Estadisticas-de-Champions-League'

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

tablas = soup.find_all('table', class_="stats_table")

# Crear una lista para almacenar los datos de las filas
filas_data = []

for table in tablas:
    for rows in table.find_all('tr')[1:]:
        row = []
        # Iterar sobre las celdas de la fila
        for cell in rows.find_all(['th', 'td']):
            # Obtener el texto de la celda y eliminar los espacios en blanco
            cell_text = ' '.join(cell.stripped_strings)
            row.append(cell_text)
        if len(row) > 0:
            filas_data.append(row)

# Seleccionar las columnas de interés
columnas_de_interes = ['rango', 'equipo', 'p_jugados', 'p_ganados', 'p_empatados', 'p_perdidos', 'goles_a_favor', 'goles_en_contra', 'diferencia_de_goles', 'puntos']
datos_seleccionados = []

for row in filas_data:
    datos_seleccionados.append(row[:10])

# Definir nombres de columnas
columnas = columnas_de_interes

# Crear el DataFrame a partir de los datos seleccionados
df = pd.DataFrame(datos_seleccionados, columns=columnas)

# Guardar el DataFrame como un archivo CSV
df.to_csv('CSV/datos_temp23_24.csv', index=False)
