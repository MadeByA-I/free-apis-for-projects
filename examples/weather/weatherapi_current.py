import requests
import json

API_KEY = "YOUR_API_KEY" # Get your free key
CITY_NAME = "Tokyo"
API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY_NAME}"

if API_KEY == "YOUR_API_KEY":
    print("Please add your WeatherAPI.com API key to the script.")
else:
    try:
        response = requests.get(API_URL)
        response.raise_for_status() # Will raise HTTPError for bad requests (4xx or 5xx)

        data = response.json()
        print(f"Current Weather in {data.get('location', {}).get('name', CITY_NAME)}:")
        current_weather = data.get('current', {})
        print(f"Condition: {current_weather.get('condition', {}).get('text', 'N/A')}")
        print(f"Temperature: {current_weather.get('temp_c', 'N/A')}°C / {current_weather.get('temp_f', 'N/A')}°F")
        print(f"Feels Like: {current_weather.get('feelslike_c', 'N/A')}°C / {current_weather.get('feelslike_f', 'N/A')}°F")
        print(f"Humidity: {current_weather.get('humidity', 'N/A')}%")
        print(f"Wind: {current_weather.get('wind_kph', 'N/A')} kph from {current_weather.get('wind_dir', 'N/A')}")

    except requests.exceptions.HTTPError as http_err:
         # Check for specific errors if API returns JSON error messages
        try:
            error_data = response.json()
            print(f"API Error: {error_data.get('error', {}).get('message', 'Unknown API error')}")
        except json.JSONDecodeError:
             print(f"HTTP error occurred: {http_err} - Could not parse error response.")
    except requests.exceptions.RequestException as e:
        # Network errors
        print(f"Network error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    except KeyError:
        print("Unexpected response format from WeatherAPI.com.")