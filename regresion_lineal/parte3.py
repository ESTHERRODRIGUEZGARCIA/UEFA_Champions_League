import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import csv


def parte3_analisis():
    # Cargar datos
    grupos_df = pd.read_csv('CSV_RL/grupos_temp_23_24.csv')
    octavos_df = pd.read_csv('CSV_RL/octavos_temp_23_24.csv')
    equipos_octavos = octavos_df['equipo'].unique()
    grupos_df['Avanzo_a_Octavos'] = grupos_df['equipo'].apply(lambda x: 1 if x in equipos_octavos else 0)

    caracteristicas = ['equipo', 'p_jugados', 'p_ganados', 'p_empatados', 'p_perdidos', 'goles_a_favor', 'goles_en_contra', 'diferencia_de_goles', 'puntos']
    etiqueta = 'Avanzo_a_Octavos'

    # Dividir datos para entrenamiento y prueba
    X = grupos_df[caracteristicas]
    y = grupos_df[etiqueta]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Pipeline para el preprocesamiento y el modelo
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', ['p_jugados', 'p_ganados', 'p_empatados', 'p_perdidos', 'goles_a_favor', 'goles_en_contra', 'diferencia_de_goles', 'puntos']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['equipo'])
        ])

    modelo = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

    # Entrenar el modelo
    modelo.fit(X_train, y_train)

    # Hacer predicciones
    predicciones = modelo.predict(X_test)

    # Calcular métricas de evaluación
    precision = precision_score(y_test, predicciones)
    recall = recall_score(y_test, predicciones)
    f1 = f1_score(y_test, predicciones)
    accuracy = accuracy_score(y_test, predicciones)

    print(f'Precision: {precision}, Recall: {recall}, F1: {f1}, Accuracy: {accuracy}')

    # Clustering
    todos_df = pd.read_csv('CSV_RL/todos.csv')

    # Convertir la columna SEASON a enteros extrayendo el primer año del rango
    todos_df['SEASON'] = todos_df['SEASON'].apply(lambda x: int(x.split('-')[0]))

    variables_clustering = ['p_jugados', 'p_ganados', 'p_empatados', 'p_perdidos', 'goles_a_favor', 'goles_en_contra', 'puntos']

    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(todos_df[variables_clustering])
    kmeans = KMeans(n_clusters=4, random_state=42)
    clusters = kmeans.fit_predict(data_normalized)

    todos_df['Cluster'] = clusters
    plt.figure(figsize=(10, 6))
    plt.hist(clusters, bins=range(5), rwidth=0.8, color='skyblue')
    plt.title('Distribución de Equipos por Clúster')
    plt.xlabel('Clúster')
    plt.ylabel('Número de Equipos')
    plt.show()

    # Ranking de equipos en función de la posesión
    data = []
    with open('semis/datos_semis.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Leer las cabeceras
        for row in reader:
            data.append(row)

    # Extraer nombres de equipos y posesiones
    equipos = [row[0] for row in data]
    posesiones = [float(row[-1]) for row in data]  # Última columna (posesión)

    # Ordenar equipos en función de la posesión
    equipos_sorted = [x for _, x in sorted(zip(posesiones, equipos))]
    posesiones_sorted = sorted(posesiones)

    # Graficar el ranking
    plt.figure(figsize=(10, 6))
    plt.barh(equipos_sorted, posesiones_sorted, color='skyblue')
    plt.xlabel('Posesión (%)')
    plt.title('Ranking de Equipos en función de la Posesión')
    plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el equipo con la mayor posesión en la parte superior
    plt.grid(axis='x')  # Agregar líneas de la cuadrícula en el eje x
    plt.show()



    # Función para cargar los datos del archivo CSV
    def cargar_datos_csv(archivo):
        try:
            with open(archivo, 'r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Leer las cabeceras
                data = [row for row in reader]
            return headers, data
        except Exception as e:
            print("Error al leer los datos del archivo CSV:", e)
            return None, None

    # Función para calcular puntajes
    # Función para calcular puntajes
    def calcular_puntajes(data, pesos, headers):
        puntajes = {}
        if data is not None:
            for row in data:
                equipo = row[0]
                stats = [float(val) if headers[i+1] in pesos else 0 for i, val in enumerate(row[1:])]
                try:
                    # Solo sumamos los puntajes para las estadísticas definidas en `pesos`
                    puntaje = sum(stats[i] * pesos.get(headers[i+1], 0) for i in range(len(stats)) if headers[i+1] in pesos)
                    puntajes[equipo] = puntaje
                except Exception as e:
                    print("Error al calcular el puntaje para", equipo, ":", e)
        return puntajes


    # Función para predecir ganadores
    def predecir_ganadores(partidos, puntajes):
        ganadores = {}
        for equipo1, equipo2 in partidos:
            try:
                puntaje1 = puntajes.get(equipo1, 0)
                puntaje2 = puntajes.get(equipo2, 0)
                ganador = equipo1 if puntaje1 > puntaje2 else equipo2
                ganadores[equipo1] = ganador
            except KeyError as e:
                print("Error al predecir el ganador para el partido entre", equipo1, "y", equipo2, ":", e)
        return ganadores

    # Archivo CSV
    archivo_csv = 'semis/datos_semis.csv'

    # Definir pesos para cada estadística (pueden ajustarse según la importancia relativa)
    pesos = {
        "media_goles_ataque": 0.6,
        "tiros_puerta": 0.2,
        "corners": 0.1,
        "posesion": 0.1
    }

    # Cargar los datos del archivo CSV
    headers, data = cargar_datos_csv(archivo_csv)

    # Si los datos se cargan correctamente, calcular puntajes y predecir ganadores
    if headers and data:
        # Partidos
        partidos = [("Real Madrid", "Bayern Munich"), ("Paris Saint-Germain", "Borussia Dortmund")]

        # Calcular puntajes para cada equipo
        puntajes = calcular_puntajes(data, pesos, headers)

        # Predecir ganadores de los partidos
        ganadores = predecir_ganadores(partidos, puntajes)

        # Imprimir resultados
        for equipo1, equipo2 in partidos:
            print(f"Ganador probable entre {equipo1} y {equipo2}: {ganadores.get(equipo1, 'No se pudo predecir')}")



    # Cargar los datos desde un archivo CSV
    archivo_csv = 'semis/datos_semis.csv'
    data = pd.read_csv(archivo_csv)

    # Configuración de la figura
    plt.figure(figsize=(12, 8))

    # Gráfico de barras para media de goles de ataque
    plt.bar(data['equipo'], data['media_goles_ataque'], color='blue', label='Media Goles Ataque')

    # Gráfico de barras para tiros a puerta
    plt.bar(data['equipo'], data['tiros_puerta'], bottom=data['media_goles_ataque'], color='green', label='Tiros a Puerta')

    # Configuración de títulos y etiquetas
    plt.xlabel('Equipos')
    plt.ylabel('Estadísticas')
    plt.title('Estadísticas de Ataque de los Equipos en Semifinales')
    plt.legend()

    # Mostrar el gráfico
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    archivo_csv = 'CSV/champions_league.csv'
    data2 = pd.read_csv(archivo_csv)
    
    campeonatos = data2['campeon'].value_counts()
    subcampeonatos = data2['subcampeon'].value_counts()

    # Mostrar las veces que el PSG y el Real Madrid han sido campeones y subcampeones
    print("Real Madrid - Campeonatos:", campeonatos.get('Real Madrid', 0))
    print("PSG - Campeonatos:", campeonatos.get('Paris Saint-Germain', 0))
    print("Real Madrid - Subcampeonatos:", subcampeonatos.get('Real Madrid', 0))
    print("PSG - Subcampeonatos:", subcampeonatos.get('Paris Saint-Germain', 0))

    def calcular_proporcion_victorias(campeonatos, subcampeonatos, equipo):
        campeonatos_equipo = campeonatos.get(equipo, 0)
        subcampeonatos_equipo = subcampeonatos.get(equipo, 0)
        total_finales = campeonatos_equipo + subcampeonatos_equipo
        if total_finales > 0:
            return campeonatos_equipo / total_finales
        else:
            return 0

    # Calcular la proporción de victorias para el PSG y el Real Madrid
    proporcion_psg = calcular_proporcion_victorias(campeonatos, subcampeonatos, 'Paris Saint-Germain')
    proporcion_rm = calcular_proporcion_victorias(campeonatos, subcampeonatos, 'Real Madrid')

    print("Proporción de victorias en finales - PSG:", proporcion_psg)
    print("Proporción de victorias en finales - Real Madrid:", proporcion_rm)

    ganador = 'PSG' if proporcion_psg > proporcion_rm else 'Real Madrid'
    print("El ganador predicho entre PSG y Real Madrid es:", ganador)

    equipos = ['PSG', 'Real Madrid']
    proporciones = [proporcion_psg, proporcion_rm]
    df_grafico = pd.DataFrame({'Equipo': equipos, 'Proporción de Victorias en Finales': proporciones})

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_grafico['Equipo'], df_grafico['Proporción de Victorias en Finales'], color=['red', 'blue'])
    plt.xlabel('Equipo')
    plt.ylabel('Proporción de Victorias en Finales')
    plt.title('Proporción de Victorias en Finales de la Champions League para PSG y Real Madrid')
    plt.ylim(0, 1)  # Limitar el eje y para mejorar la visualización
    plt.show()

if __name__ == '__main__':
    parte3_analisis()
