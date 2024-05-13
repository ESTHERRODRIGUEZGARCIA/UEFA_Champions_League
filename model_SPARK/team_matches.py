import requests
import json

api_key = '5efeea68fa60416cad757ca4d1cb0d79'
base_url = "http://api.football-data.org/v2/"
headers = {'X-Auth-Token': api_key}

# Diccionario de IDs de los equipos
team_ids = {'Real Madrid': 86, 'Bayern Munich': 5, 'PSG': 524, 'Dortmund': 4}

# Recopilar datos de partidos para cada equipo
team_matches = {}
for team, team_id in team_ids.items():
    url = f"{base_url}teams/{team_id}/matches"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        team_matches[team] = response.json()
    else:
        print(f"Failed to fetch matches for {team}")

# Optional: Guardar los datos en un archivo para evitar múltiples llamadas a la API
with open('SPARK/team_matches.json', 'w') as f:
    json.dump(team_matches, f, indent=4)
