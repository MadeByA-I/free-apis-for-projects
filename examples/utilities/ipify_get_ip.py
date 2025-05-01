import requests
import json

# Use format=json to get a JSON response
API_URL = "https://api.ipify.org?format=json"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Your public IP address is: {data.get('ip', 'N/A')}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")