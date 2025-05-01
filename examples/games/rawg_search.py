import requests
import json

API_KEY = "YOUR_API_KEY" # Get your free key from rawg.io (needs an account)
SEARCH_TERM = "Cyberpunk 2077"
API_URL = f"https://api.rawg.io/api/games?key={API_KEY}&search={SEARCH_TERM}&page_size=5"

if API_KEY == "YOUR_API_KEY":
    print("Please add your RAWG API key to the script.")
else:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()
        print(f"Top Game Search Results for '{SEARCH_TERM}':")
        if 'results' in data and data['results']:
            for game in data['results']:
                name = game.get('name', 'N/A')
                rating = game.get('rating', 'N/A')
                released = game.get('released', 'N/A')
                print(f"- {name} (Rating: {rating}, Released: {released})")
        else:
            print("No results found or unexpected format.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except (json.JSONDecodeError, KeyError):
        print("Error processing response.")