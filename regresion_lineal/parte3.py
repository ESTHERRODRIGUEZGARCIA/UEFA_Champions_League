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



if __name__ == '__main__':
    parte3_analisis()
