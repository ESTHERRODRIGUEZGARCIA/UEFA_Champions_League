import requests

token = "5efeea68fa60416cad757ca4d1cb0d79"

# Endpoint para obtener equipos de una competición específica (p.ej., La Liga)
url_teams = "http://api.football-data.org/v2/competitions/PD/teams"  # 'PD' es el código de La Liga

headers = {"X-Auth-Token": token}

# Primero, obtenemos los equipos de La Liga
response_teams = requests.get(url_teams, headers=headers)

if response_teams.status_code == 200:
    teams_data = response_teams.json()
    # Buscamos el ID de Real Madrid entre los equipos
    for team in teams_data['teams']:
        if team['name'] == "Real Madrid CF":
            real_madrid_id = team['id']
            print("ID de Real Madrid:", real_madrid_id)
            break
else:
    print("Error al obtener equipos:", response_teams.status_code)
