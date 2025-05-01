import requests
import json

PRODUCT_ID = 1
API_URL = f"https://fakestoreapi.com/products/{PRODUCT_ID}"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Details for Product #{PRODUCT_ID}:")
    print(f"Title: {data.get('title', 'N/A')}")
    print(f"Price: ${data.get('price', 'N/A')}")
    print(f"Description: {data.get('description', 'N/A')[:100]}...")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")