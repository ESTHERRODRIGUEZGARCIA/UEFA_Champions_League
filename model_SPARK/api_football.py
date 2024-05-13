import requests
import json

# Configura tu API Key
api_key = '5efeea68fa60416cad757ca4d1cb0d79'
url = "http://api.football-data.org/v2/competitions/CL/teams"
headers = {'X-Auth-Token': api_key}

response = requests.get(url, headers=headers)
teams = response.json()

# Filtra para obtener solo los equipos de interés por nombre
interested_teams = ['Real Madrid CF', 'FC Bayern München', 'Paris Saint-Germain FC', 'Borussia Dortmund']
filtered_teams = {team['name']: team['id'] for team in teams['teams'] if team['name'] in interested_teams}

print(filtered_teams)
