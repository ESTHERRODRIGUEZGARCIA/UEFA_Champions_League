import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def modelo_regresion_lineal_uefa():
    # Cargar y preparar los datos
    df_resultados_23_24 = pd.read_csv('CSV_RL/resultados_23_24.csv')
    df_global_temp_con_puntos = pd.read_csv('temporadas/global_temp_con_puntos.csv')

    # Concatenar y ordenar los DataFrames
    df_todos = pd.concat([df_resultados_23_24, df_global_temp_con_puntos])
    df_todos = df_todos.sort_values(by='SEASON')
    df_todos.to_csv('CSV_RL/todos.csv', index=False)

    df_todos = pd.read_csv('CSV_RL/todos.csv')

    # Mostrar la gráfica visual de la matriz de correlaciones
    matriz = df_todos.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, cbar=True)
    plt.title('Matriz de Correlaciones entre Variables')
    plt.show()

    # Definir las variables independientes (X) y la variable dependiente (y)
    X = df_todos[['p_ganados', 'p_perdidos', 'goles_a_favor', 'goles_en_contra']]
    y = df_todos['puntos']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Crear y entrenar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Hacer predicciones
    y_pred = modelo.predict(X_test)

    # Calcular métricas de evaluación
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'MAE: {mae}, MSE: {mse}, R2: {r2}')

    # Visualización del ranking
    df_resultados_23_24 = df_resultados_23_24.sort_values(by='puntos', ascending=False)
    plt.figure(figsize=(10, 8))
    sns.barplot(x='puntos', y='equipo', data=df_resultados_23_24, palette='viridis')
    plt.title('Ranking de Equipos')
    plt.show()

    # Visualización del rendimiento de los 16 equipos en octavos de final
    equipos_octavos = df_resultados_23_24.head(16)
    plt.figure(figsize=(10, 8))
    sns.barplot(x='puntos', y='equipo', data=equipos_octavos, palette='plasma')
    plt.title('Rendimiento de los 16 Equipos en Octavos de Final')
    plt.show()

    # Calcular y mostrar las probabilidades estimadas de ganar la Champions League
    puntajes = {}
    equipos = equipos_octavos['equipo'].values

    for equipo in equipos:
        puntajes[equipo] = df_todos[df_todos['equipo'] == equipo]['puntos'].mean()

    puntajes_ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    equipos = [equipo[0] for equipo in puntajes_ordenados]
    puntajes_equipo = [puntaje[1] for puntaje in puntajes_ordenados]

    plt.figure(figsize=(10, 8))
    plt.barh(equipos, puntajes_equipo, color='skyblue')
    plt.xlabel('Puntaje')
    plt.title('Probabilidades Estimadas de Ganar la Champions League 2023-2024')
    plt.gca().invert_yaxis()
    plt.show()

    # Convertir a porcentajes y graficar
    total_puntos = sum(puntajes_equipo)
    porcentajes_equipo = [(puntaje / total_puntos) * 100 for puntaje in puntajes_equipo]

    plt.figure(figsize=(10, 8))
    plt.barh(equipos, porcentajes_equipo, color='lightgreen')
    plt.xlabel('Porcentaje (%)')
    plt.title('Probabilidades Estimadas de Ganar la Champions League 2023-2024 (%)')
    plt.gca().invert_yaxis()
    plt.show()

    print("Porcentajes de los equipos:")
    for equipo, porcentaje in zip(equipos, porcentajes_equipo):
        print(f"{equipo}: {porcentaje:.2f}%")


