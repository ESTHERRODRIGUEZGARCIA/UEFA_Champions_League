# main.py
from model_AB.analisis_arbol_bosque import model_a_b
from model_AB.visual import grafica_model_a_b
from semis.stats import *
from Parte3.modelo_arima import model_arima
from Parte3.modelo2_arima import model2_arima
from RedesNeuronales.prob_semis import *
from regresion_lineal.reg_lin import modelo_regresion_lineal_uefa
from regresion_lineal.parte3 import parte3_analisis



def main():
    while True:
        print("Seleccione el módulo de análisis a ejecutar:")
        print("1. regresión lineal (Probabilidades Estimadas de Ganar la Champions League 2023-2024 desde octavos (%))")
        print("2. regresión lineal con un ganador final")
        print("3. Redes Neuronales")
        print("4. Análisis de Árbol y Bosque")
        print("5. Análisis de Datos con series temporales")
        print("6. Gráficas de estadísticas de los equipos semifinalistas ")
        print("7. INTENTO (no conseguido): Análisis Avanzado con LangChain y Llama 3")
        print("8. INTENTO (no conseguido): Análisis de Datos con Spark")

        choice = input("Ingrese su opción: ")
        if choice == "1":
            modelo_regresion_lineal_uefa()
        elif choice == "2":
            parte3_analisis()
        elif choice == "3":
            probabilidad_semis()
        elif choice == "4":
            model_a_b()
            grafica_model_a_b()
        elif choice == "5":
            print("Primera opción: Modelo autorregresivo integrado de media móvil (ARIMA)")
            model_arima()
            model2_arima()
        elif choice == "6":
            graficas_semis()

        repetir = input("¿Quieres ejecutar otro modelo? Sí:1 No:2 \n")
        if repetir == "2":
            break
        else:
            continue



if __name__ == "__main__":
    main()



#añadir un apartado de graficas sobre las semis: stats.py