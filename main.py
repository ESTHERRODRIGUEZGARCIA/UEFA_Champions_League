# main.py
from model_LLAMA3 import *
from modelo_2 import *
from Parte3 import *
from RedesNeuronales import *
from regresion_lineal import *
from semis.stats import *
from model_SPARK import *
import analisis_arbol_bosque
import advanced_analysis

def main():
    print("Seleccione el módulo de análisis a ejecutar:")
    print("1. regresión lineal (Probabilidades Estimadas de Ganar la Champions League 2023-2024 (%))")
    print("2. Análisis Avanzado con LangChain y Llama 3")
    print("3. Regresión Lineal")
    print("4. Redes Neuronales")
    print("5. Análisis de Árbol y Bosque")
    print("6. Análisis de Datos con Spark")
    print("7. Análisis de Datos con Pandas")
    print("8. Gráficas de estadísticas de los equipos semifinalistas ")
    choice = input("Ingrese su opción: ")
    if choice == "1":
        regresion_lineal()
    elif choice == "8":
        semis.stats()

    

if __name__ == "__main__":
    main()



#añadir un apartado de graficas sobre las semis: stats.py