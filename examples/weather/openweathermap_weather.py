import requests
import json

API_KEY = "YOUR_API_KEY" # Get your free key
CITY_NAME = "London"
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric" # units=metric for Celsius

if API_KEY == "YOUR_API_KEY":
    print("Please add your OpenWeatherMap API key to the script.")
else:
    try:
        response = requests.get(API_URL)
        response.raise_for_status() # Checks for 4xx/5xx errors

        # Handle specific API errors (like invalid key or city not found)
        if response.status_code == 401:
             print("Error: Invalid API Key.")
        elif response.status_code == 404:
             print(f"Error: City '{CITY_NAME}' not found.")
        else:
            data = response.json()
            print(f"Weather in {data.get('name', CITY_NAME)}:")
            if 'weather' in data and data['weather']:
                print(f"Condition: {data['weather'][0].get('description', 'N/A')}")
            if 'main' in data:
                print(f"Temperature: {data['main'].get('temp', 'N/A')}°C")
                print(f"Humidity: {data['main'].get('humidity', 'N/A')}%")
            if 'wind' in data:
                 print(f"Wind Speed: {data['wind'].get('speed', 'N/A')} m/s")

    except requests.exceptions.RequestException as e:
        # Network errors
        print(f"Network error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    except KeyError:
        print("Unexpected response format from OpenWeatherMap.")