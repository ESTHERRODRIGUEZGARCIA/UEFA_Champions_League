# main.py
import data_loader
import analisis_arbol_bosque
import advanced_analysis
import linear_regression

def main():
    print("Seleccione el módulo de análisis a ejecutar:")
    print("1. Análisis Básico")
    print("2. Análisis Avanzado con LangChain y Llama 3")
    print("3. Regresión Lineal")
    choice = input("Ingrese su opción: ")
    
    if choice == '1':
        analisis_arbol_bosque.run_basic_analysis()
    elif choice == '2':
        advanced_analysis.run_advanced_analysis()
    elif choice == '3':
        linear_regression.run_regression_analysis()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()



#añadir un apartado de graficas sobre las semis: stats.py