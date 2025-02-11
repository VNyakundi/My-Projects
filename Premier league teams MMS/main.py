from flask import Flask, render_template
import requests

# Flask App
app = Flask(__name__)

# API Configuration
API_URL = "https://v3.football.api-sports.io/standings"
API_KEY = "2243e6d8099209e3fbe01902bad4262d"
LEAGUE_ID = 39  # Premier League (API-Football league ID)
SEASON = 2024  # Current season


class PremierLeagueAPI:
    """Handles API requests to fetch Premier League standings"""

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"x-apisports-key": self.api_key}

    def get_standings(self):
        """Fetch Premier League standings"""
        response = requests.get(API_URL, headers=self.headers, params={"league": LEAGUE_ID, "season": SEASON})

        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            return []  # Return empty list if API request fails

        data = response.json()

        # 🔴 Debugging: Print API response
        print("API Response:", data)

        # Validate API response structure
        if "response" not in data or not data["response"]:
            print("Error: API response is empty or invalid!")
            return []

        try:
            return data["response"][0]["league"]["standings"][0]  # Extract standings
        except (IndexError, KeyError) as e:
            print(f"Error: Unexpected API response structure -> {e}")
            return []


class Team:
    """Represents a football team in the Premier League standings"""

    def __init__(self, rank, name, points, played, wins, draws, losses, goal_diff, logo):
        self.rank = rank
        self.name = name
        self.points = points
        self.played = played
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goal_diff = goal_diff
        self.logo = logo


class LeagueTable:
    """Processes and structures Premier League standings"""

    def __init__(self, standings_data):
        self.teams = [
            Team(
                team["rank"],
                team["team"]["name"],
                team["points"],
                team["all"]["played"],
                team["all"]["win"],
                team["all"]["draw"],
                team["all"]["lose"],
                team["goalsDiff"],
                team["team"]["logo"],
            )
            for team in standings_data
        ]


@app.route("/")
def home():
    """Fetch and display Premier League table"""
    api = PremierLeagueAPI(API_KEY)
    standings_data = api.get_standings()

    # If no data is returned, display an error page or message
    if not standings_data:
        return render_template("error.html", message="No data available for the current season.")

    league_table = LeagueTable(standings_data)
    return render_template("index.html", teams=league_table.teams)


if __name__ == "__main__":
    app.run(debug=True)
