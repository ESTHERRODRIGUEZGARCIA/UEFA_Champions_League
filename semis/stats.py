import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Establecer el estilo de los gráficos para todo el archivo
sns.set(style="whitegrid")
def graficas_semis():

    # Datos y gráfico de semifinales
    datos_semis_df = pd.read_csv('semis/datos_semis.csv')
    plt.figure(figsize=(14, 7))
    plt.subplot(1, 2, 1)
    sns.histplot(datos_semis_df['media_goles_ataque'], kde=True, color='blue', binwidth=0.1)
    plt.title('Distribución de Media de Goles de Ataque')
    plt.subplot(1, 2, 2)
    sns.histplot(datos_semis_df['goles_recibidos'], kde=True, color='red', binwidth=0.1)
    plt.title('Distribución de Goles Recibidos')
    plt.tight_layout()
    plt.show()

    # Posesión de balón
    file_path = 'semis/equipos_con_mayor_posesion_de_balon.csv'
    data = pd.read_csv(file_path, delimiter=';', skipinitialspace=True)
    data = data.dropna()  # Elimina filas con valores NaN
    data.columns = data.columns.str.strip()  # Limpia espacios en los nombres de columnas
    data['Parámetro'] = data['Parámetro'].str.strip()  # Limpia los nombres de los equipos
    data['Posesión (%)'] = data['Posesión (%)'].astype(str).str.extract('(\d+)').astype(float)  # Extrae y convierte el porcentaje de posesión a float
    plt.figure(figsize=(10, 6))
    plt.bar(data['Parámetro'], data['Posesión (%)'], color='skyblue')
    plt.xlabel('Equipos')
    plt.ylabel('Posesión (%)')
    plt.title('Posesión de Balón de los Equipos en 2024')
    plt.ylim(0, 100)  # Define el límite del eje Y para claridad
    plt.show()




    # Número de victorias
    data_victories = pd.read_csv('semis/equipos_con_mas_victorias.csv', delimiter=';', skipinitialspace=True)
    data_victories.dropna(inplace=True)
    data_victories.columns = data_victories.columns.str.strip()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Parámetro', y='Victorias', data=data_victories, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Número de Victorias')
    plt.title('Número de Victorias por Equipo en 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Goles anotados
    data_goleadores = pd.read_csv('semis/equipos_mas_goleadores.csv', delimiter=';', skipinitialspace=True)
    data_goleadores.dropna(inplace=True)
    data_goleadores.columns = data_goleadores.columns.str.strip()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Parámetro', y='Goles', data=data_goleadores, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Goles Anotados')
    plt.title('Goles Anotados por Equipos en 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Acierto en pases
    data_pases = pd.read_csv('semis/equipos_con_mas_acierto_en_sus_pases.csv', delimiter=';', skipinitialspace=True)
    data_pases.columns = data_pases.columns.str.strip()
    data_pases.dropna(inplace=True)
    data_pases['Pases completados (%)'] = data_pases['Pases completados (%)'].str.replace(',', '.').astype(float)  # Convertir a float
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Parámetro', y='Pases completados (%)', data=data_pases, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Porcentaje de Pases Completados')
    plt.title('Acierto en Pases de Equipos en 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Remates totales y a puerta
    data_rematan = pd.read_csv('semis/equipos_que_mas_rematan.csv', delimiter=';', skipinitialspace=True)
    data_rematan.dropna(inplace=True)
    data_rematan.columns = data_rematan.columns.str.strip()
    plt.figure(figsize=(14, 7))
    plt.subplot(1, 2, 1)
    sns.barplot(x='Parámetro', y='Remates', data=data_rematan, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Remates Totales')
    plt.title('Remates Totales por Equipos en 2024')
    plt.xticks(rotation=45)
    plt.subplot(1, 2, 2)
    sns.barplot(x='Parámetro', y='A puerta', data=data_rematan, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Remates a Puerta')
    plt.title('Remates a Puerta por Equipos en 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Goles en contra
    data_menos_goleados = pd.read_csv('semis/equipos_menos_goleados.csv', delimiter=';', skipinitialspace=True)
    data_menos_goleados.dropna(inplace=True)
    data_menos_goleados.columns = data_menos_goleados.columns.str.strip()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Parámetro', y='Goles en contra', data=data_menos_goleados, palette='coolwarm')
    plt.xlabel('Equipos')
    plt.ylabel('Goles en Contra')
    plt.title('Goles en Contra por Equipos en 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
