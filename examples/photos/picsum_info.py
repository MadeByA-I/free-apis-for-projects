import requests
import json

IMAGE_ID = 0 # Change to get info for a different image
API_URL = f"https://picsum.photos/id/{IMAGE_ID}/info"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Info for Picsum Image ID #{IMAGE_ID}:")
    print(f"Author: {data.get('author', 'N/A')}")
    print(f"Width: {data.get('width', 'N/A')}")
    print(f"Height: {data.get('height', 'N/A')}")
    print(f"URL: {data.get('url', 'N/A')}")
    print(f"Download URL: {data.get('download_url', 'N/A')}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")