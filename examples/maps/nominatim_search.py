import requests
import json

SEARCH_PLACE = "Eiffel Tower, Paris"
# IMPORTANT: Provide a descriptive User-Agent
HEADERS = {'User-Agent': 'CoolProjectBot/1.0 (YourContactInfoHere)'} # Change this!
API_URL = f"https://nominatim.openstreetmap.org/search?q={SEARCH_PLACE}&format=json&limit=1"

try:
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()

    data = response.json()
    print(f"Geocoding Result for '{SEARCH_PLACE}':")
    if data and isinstance(data, list):
        location = data[0]
        print(f"Display Name: {location.get('display_name', 'N/A')}")
        print(f"Latitude: {location.get('lat', 'N/A')}")
        print(f"Longitude: {location.get('lon', 'N/A')}")
    else:
        print("No results found or unexpected format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, IndexError, KeyError):
    print("Error processing response.")