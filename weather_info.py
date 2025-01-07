import requests
import os

def fetch_weather_data(city: str, api_key: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric"
    }
    response = requests.get(base_url, params = params)
    response.raise_for_status()
    return response.json()

def parse_weather_data(data):
    try:
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        return {
            "temperature" : temperature,
            "weather": weather,
            "humidity": humidity
        }
    except KeyError as e:
        raise ValueError(f"Invalid reponse format: Missing key {e}")

def get_weather(city: str):
    # openweathermap API KEY
    api_key = os.getenv("API_KEY_OPEN_WEATHER_MAP")

    try:
        # Make the API Call
        data = fetch_weather_data(city, api_key)
        weather_info = parse_weather_data(data)

        print(f"Weather in {city}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Condition: {weather_info['weather'].capitalize()}")
        print(f"Humidity: {weather_info['humidity']}%")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    city = input("Enter the city name:")
    get_weather(city)