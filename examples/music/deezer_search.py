import requests
import json

SEARCH_ARTIST = "Queen"
API_URL = f"https://api.deezer.com/search/artist?q={SEARCH_ARTIST}&limit=5"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Top 5 Artist Search Results for '{SEARCH_ARTIST}':")
    if 'data' in data and data['data']:
        for artist in data['data']:
            print(f"- {artist.get('name', 'N/A')} (ID: {artist.get('id', 'N/A')})")
    else:
        print("No results found or unexpected format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")