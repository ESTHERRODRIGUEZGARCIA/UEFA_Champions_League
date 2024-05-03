import requests
import pandas as pd

api_key = '5efeea68fa60416cad757ca4d1cb0d79'
url = "http://api.football-data.org/v2/teams/86/matches"  # ID de Real Madrid
headers = {'X-Auth-Token': api_key}
response = requests.get(url, headers=headers)
matches = response.json()['matches']

df = pd.DataFrame(matches)
df.to_csv('SPARK/real_madrid_matches.csv', index=False)
