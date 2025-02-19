import requests

API_KEY = "e8989ef9f666bc107476508c03ca394c"
HEADERS = {
    "x-apisports-key": "e8989ef9f666bc107476508c03ca394c",
    "Accept": "application/json"
}

# API Endpoints for the year 2023
url_top_scorers = "https://v3.football.api-sports.io/players/topscorers?league=39&season=2023"
url_standings = "https://v3.football.api-sports.io/standings?league=39&season=2023"

# Function to fetch API data

def fetch_data(url,description):
    responce = requests.get(url,headers=HEADERS)
    if responce.status_code==200:
        data = responce.json()
        if "errors" in data and data ['errors']:
            print(f"Error fetching{description}:{data['errors']}")
        else:
            return data
    else:
        print(f"Error fetching{description}:{responce.status_code}")
    return None

# Function to display top scorers

def display_top_scorers(data):
    if not data or  "responce" not in data:
        print("no data available")
        return
    print("\n⚽ **Top Scorers - EPL 2023** ⚽")
    for player in data['responce'][0]:
        name = player['player']['name']
        goals = player['statistics'][0]['goals']['total']
        club = player['statistics'][0]['team']['name']
        print(f"{name}({club})- {goals} Goals")

# function to display team standings

def display_standings(data):
    if not data or "responce" not in data:
        print("no data available")
        return
    print("\n🏆 **EPL 2023 Standings** 🏆")
    standings = data['responce'][0]["league"]['standings']
    for team in standings:
        rank = team['rank']
        name = team["name"]['name']
        points = team['points']
        print(f"{rank}.{name}-{points} points")

# Fetch and display data 
top_scorers_data = fetch_data(url_top_scorers, "top scorers")
display_top_scorers(top_scorers_data)

standings_data = fetch_data(url_standings, "standings")
display_standings(standings_data)






