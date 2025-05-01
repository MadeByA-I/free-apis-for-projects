import requests
import json

API_URL = "https://catfact.ninja/fact"

try:
    response = requests.get(API_URL)
    response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

    data = response.json()
    print("Random Cat Fact:")
    print(data['fact'])

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
except KeyError:
    print("Unexpected response format.")