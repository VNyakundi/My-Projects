import requests

API_KEY = "204be5e8abd24038113ffb2ca973d756"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """fetches weather data from a given city"""
    params = {"q":city, "appid":API_KEY,
              "units":"metric"}
    responce = requests.get(BASE_URL,params=params)
    if responce.status_code==200:
        data = responce.json()
        weather = {
            "city":data["name"],
            "temperature":data["main"]["temp"],
            "humidity":data["main"]
["humidity"],
             "description":data["weather"][0]
["description"]
        }
        return weather
    else:
        return{"error":"city not found"}
    

city_name = input("Enter city name: ")
weather_info = get_weather(city_name)

if "error" in weather_info:
    print(weather_info["error"])
else:
    print(f"weather in {weather_info['city']}:")
    print(f"Temperature:{weather_info['temperature']}°C")
    print(f"Humidity:{weather_info['humidity']}%")
    print(f"Condition:{weather_info['description'].capitalize()}")