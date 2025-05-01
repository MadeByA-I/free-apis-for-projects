import requests
import json

# Get a free API key from https://thedogapi.com/
API_KEY = "YOUR_API_KEY" # Optional for random image, required for breeds etc.
API_URL = "https://api.thedogapi.com/v1/images/search"

headers = {
    'x-api-key': API_KEY
}

try:
    # Set headers=headers if using API key features
    response = requests.get(API_URL) # Add headers=headers if needed
    response.raise_for_status()

    data = response.json()
    if data and isinstance(data, list):
        print("Random Dog Image URL:")
        print(data[0]['url'])
    else:
        print("Unexpected response format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, IndexError, KeyError):
    print("Error processing response.")