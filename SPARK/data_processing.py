import pandas as pd
from data_fetcher import fetch_matches

def create_dataframe():
    matches_data = fetch_matches()
    if 'matches' in matches_data:
        matches_list = matches_data['matches']
        df = pd.json_normalize(matches_list)
        return df
    else:
        print("No se encontraron datos de 'matches'.")
        return pd.DataFrame()
