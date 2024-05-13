import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def model_a_b():
        

    # Cargar datos
    datos_semis = pd.read_csv('datos_gradio/datos_semis.csv')
    global_temp_con_puntos = pd.read_csv('datos_gradio/global_temp_con_puntos.csv')

    # Supongamos que queremos crear una columna 'alta_probabilidad_ganar' basada en ciertos criterios
    datos_semis['alta_probabilidad_ganar'] = ((datos_semis['posesion'] >= 50) & (datos_semis['media_goles_ataque'] > 1.75)).astype(int)

    # Filtrar los datos históricos para incluir solo equipos en semifinales y las últimas temporadas
    equipos_semis = datos_semis['equipo'].tolist()
    global_temp_filtrado_extendido = global_temp_con_puntos[
        global_temp_con_puntos['equipo'].isin(equipos_semis) &
        global_temp_con_puntos['SEASON'].isin(['2022-2023', '2021-2022'])
    ]

    # Preparar datos acumulados históricos
    datos_acumulados = global_temp_filtrado_extendido.groupby('equipo').agg({
        'p_jugados': 'sum',
        'p_ganados': 'sum',
        'p_empatados': 'sum',
        'p_perdidos': 'sum',
        'goles_a_favor': 'sum',
        'goles_en_contra': 'sum',
        'puntos': 'sum'
    }).reset_index()

    # Combinar datos de 'datos_semis' con 'datos_acumulados'
    datos_finales = pd.merge(datos_semis, datos_acumulados, on='equipo', how='left')

    # Manejar valores nulos
    imputer = SimpleImputer(strategy='mean')
    datos_finales_imputed = pd.DataFrame(imputer.fit_transform(datos_finales.drop(['equipo'], axis=1)),
                                        columns=datos_finales.drop(['equipo'], axis=1).columns)

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_full = datos_finales_imputed.drop('alta_probabilidad_ganar', axis=1)
    y_full = datos_finales_imputed['alta_probabilidad_ganar']

    X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_full, y_full, test_size=0.5, random_state=42)

    # Entrenar un Árbol de Decisión
    tree_model_full = DecisionTreeClassifier(random_state=42)
    tree_model_full.fit(X_train_full, y_train_full)

    # Entrenar un Bosque Aleatorio
    forest_model_full = RandomForestClassifier(n_estimators=100, random_state=42)
    forest_model_full.fit(X_train_full, y_train_full)

    # Predecir los resultados del conjunto de prueba
    tree_predictions_full = tree_model_full.predict(X_test_full)
    forest_predictions_full = forest_model_full.predict(X_test_full)

    # Evaluar los modelos
    tree_accuracy_full = accuracy_score(y_test_full, tree_predictions_full)
    forest_accuracy_full = accuracy_score(y_test_full, forest_predictions_full)

    print("Árbol de Decisión Precisión:", tree_accuracy_full)
    print("Bosque Aleatorio Precisión:", forest_accuracy_full)

    # Obtener probabilidades de ganar utilizando el modelo de bosque aleatorio
    probabilidades = forest_model_full.predict_proba(X_full)[:, 1]  # Probabilidad de la clase 1 (alta probabilidad de ganar)
    datos_finales['probabilidad_ganar'] = probabilidades

    # Simular enfrentamientos de semifinales y final
    # Real Madrid vs Bayern Munich y PSG vs Borussia Dortmund
    semifinal_1_ganador = 'Real Madrid' if datos_finales.loc[datos_finales['equipo'] == 'Real Madrid', 'probabilidad_ganar'].values[0] > \
                                        datos_finales.loc[datos_finales['equipo'] == 'Bayern Munich', 'probabilidad_ganar'].values[0] else 'Bayern Munich'
    semifinal_2_ganador = 'Paris Saint-Germain' if datos_finales.loc[datos_finales['equipo'] == 'Paris Saint-Germain', 'probabilidad_ganar'].values[0] > \
                                                datos_finales.loc[datos_finales['equipo'] == 'Borussia Dortmund', 'probabilidad_ganar'].values[0] else 'Borussia Dortmund'
    campeon = semifinal_1_ganador if datos_finales.loc[datos_finales['equipo'] == semifinal_1_ganador, 'probabilidad_ganar'].values[0] > \
                                    datos_finales.loc[datos_finales['equipo'] == semifinal_2_ganador, 'probabilidad_ganar'].values[0] else semifinal_2_ganador

    print("Semifinal 1 Ganador:", semifinal_1_ganador)
    print("Semifinal 2 Ganador:", semifinal_2_ganador)
    print("Campeón de la Champions League:", campeon)
