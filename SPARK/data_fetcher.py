import requests
from config import API_KEY

def fetch_matches():
    url = "http://api.football-data.org/v2/competitions/CL/matches"
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(url, headers=headers)
    matches = response.json()
    return matches
