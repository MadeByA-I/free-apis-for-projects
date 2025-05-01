import requests
import json

SEARCH_TERM = "Dune" # Change to search for different books
API_URL = f"https://openlibrary.org/search.json?q={SEARCH_TERM}&limit=5"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print(f"Top 5 Book Search Results for '{SEARCH_TERM}':")
    if 'docs' in data and data['docs']:
        for book in data['docs']:
            title = book.get('title', 'N/A')
            author = ", ".join(book.get('author_name', ['N/A']))
            year = book.get('first_publish_year', 'N/A')
            print(f"- {title} by {author} ({year})")
    else:
        print("No results found or unexpected format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")