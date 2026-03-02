# database.py

import json

def save_to_file(books, filename='library_data.json'):
    """Save the books list to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(books, file)
    print('Library data saved.')

def load_from_file(filename='library_data.json'):
    """Load books data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []