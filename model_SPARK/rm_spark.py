import requests
import pandas as pd
import os

def fetch_team_matches(team_id, api_key):
    url = f"http://api.football-data.org/v2/teams/{team_id}/matches"
    headers = {'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    matches = response.json()['matches']
    return matches

api_key = '5efeea68fa60416cad757ca4d1cb0d79'
teams = {
    'Real Madrid': 86,
    'Bayern Munich': 5,
    'PSG': 524,
    'Dortmund': 4
}

matches_data = {}
for team, team_id in teams.items():
    matches_data[team] = fetch_team_matches(team_id, api_key)

# Crear la carpeta SPARK si no existe
carpeta_resultados = 'SPARK'
if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)

# Convertir los datos a DataFrame y guardar
for team, matches in matches_data.items():
    df = pd.DataFrame(matches)
    archivo_csv = os.path.join(carpeta_resultados, f'{team}_matches.csv')
    df.to_csv(archivo_csv, index=False)