import requests
import json

POST_ID = 1
API_URL = f"https://jsonplaceholder.typicode.com/posts/{POST_ID}"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Details for Post #{POST_ID}:")
    print(f"Title: {data.get('title', 'N/A')}")
    print(f"Body: {data.get('body', 'N/A')[:100]}...") # Print first 100 chars

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")