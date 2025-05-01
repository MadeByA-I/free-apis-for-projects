import requests
import json

# Endpoint for programming jokes, see repo for others
API_URL = "https://official-joke-api.appspot.com/jokes/programming/random"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    # This API returns a list containing one joke
    data = response.json()
    if data and isinstance(data, list):
        joke = data[0]
        print("Random Programming Joke:")
        print(f"Setup: {joke.get('setup', 'N/A')}")
        print(f"Punchline: {joke.get('punchline', 'N/A')}")
    else:
        print("Unexpected response format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, IndexError, KeyError):
    print("Error processing response.")