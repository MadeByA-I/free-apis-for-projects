import requests
import json

SEARCH_TERM = "Naruto" # Change to search for different anime
API_URL = f"https://api.jikan.moe/v4/anime?q={SEARCH_TERM}&limit=5"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Top 5 Anime Search Results for '{SEARCH_TERM}':")
    if 'data' in data and data['data']:
        for anime in data['data']:
            print(f"- {anime['title']} (Score: {anime.get('score', 'N/A')})")
    else:
        print("No results found or unexpected format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")