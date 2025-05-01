import requests
import json

# Use DEMO_KEY for basic testing, but get your own key for real use
API_KEY = "DEMO_KEY" 
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

if API_KEY == "DEMO_KEY":
    print("Using DEMO_KEY. Get your own key from api.nasa.gov for higher rate limits.")

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print("NASA Astronomy Picture of the Day:")
    print(f"Date: {data.get('date', 'N/A')}")
    print(f"Title: {data.get('title', 'N/A')}")
    print(f"Explanation: {data.get('explanation', 'N/A')[:200]}...") # First 200 chars
    print(f"Image URL: {data.get('url', 'N/A')}") # Might be video link too

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")