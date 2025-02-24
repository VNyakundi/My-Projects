from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    if request.method == "POST":
        city = request.form["city"]
        weather_info = get_weather(city)
    
    return render_template("index.html", weather=weather_info)

if __name__ == "__main__":
    app.run(debug=True)