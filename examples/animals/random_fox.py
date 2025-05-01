import requests
import json

API_URL = "https://randomfox.ca/floof/"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print("Random Fox Image URL:")
    print(data['image'])

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
except KeyError:
    print("Unexpected response format.")