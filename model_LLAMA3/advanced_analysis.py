#f4798afc56c3494494604165739b7df9

# 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
import pandas as pd
import os
from langchain.llmchains import LLMChain  # Asume una importación genérica; ajusta según la documentación

# Carga de datos
def load_data():
    champions_league_df = pd.read_csv('daatos_gradio/champions_league.csv')
    return champions_league_df

# Función principal para realizar consultas y generar respuestas
def main():
    # Cargar datos
    data = load_data()

    # Configurar la API key y el modelo Llama3, ajustar según la documentación real
    os.environ['OPENAI_API_KEY'] = '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'
    llm = LLMChain(model="llama-3", api_key=os.environ['OPENAI_API_KEY'])

    # Ejemplo de consulta sobre los datos
    prompt = "¿Quién ganó la Champions League en 2021?"
    winner_2021 = data[data['temporada'] == '2020-2021']['campeon'].iloc[0]
    response = llm.generate(prompt)  # Asume que `generate` es el método correcto; verifica la documentación

    print("Respuesta del modelo:", response)
    print("Ganador según los datos:", winner_2021)

if __name__ == "__main__":
    main()
