import requests
import json
import html # To decode HTML entities

API_URL = "https://opentdb.com/api.php?amount=1&type=multiple" # Get 1 multiple choice question

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    print("Random Trivia Question:")
    if 'results' in data and data['results']:
        question_data = data['results'][0]
        question = html.unescape(question_data.get('question', 'N/A'))
        correct_answer = html.unescape(question_data.get('correct_answer', 'N/A'))
        incorrect_answers = [html.unescape(ans) for ans in question_data.get('incorrect_answers', [])]
        
        print(f"Category: {html.unescape(question_data.get('category', 'N/A'))}")
        print(f"Question: {question}")
        # Combine and shuffle options for display if needed
        options = incorrect_answers + [correct_answer]
        # import random; random.shuffle(options) # Optional: Shuffle options
        print(f"Options: {options}")
        print(f"Correct Answer: {correct_answer}") # Keep this separate for checking
    else:
        print("No results found or unexpected format.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except (json.JSONDecodeError, KeyError):
    print("Error processing response.")