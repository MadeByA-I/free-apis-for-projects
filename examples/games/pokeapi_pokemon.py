import requests
import json

POKEMON_NAME = "ditto" # Change to get different Pokémon (use lowercase)
API_URL = f"https://pokeapi.co/api/v2/pokemon/{POKEMON_NAME}"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Details for Pokémon: {data.get('name', 'N/A').capitalize()}")
    print(f"ID: {data.get('id', 'N/A')}")
    types = [t['type']['name'] for t in data.get('types', [])]
    print(f"Types: {', '.join(types)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")