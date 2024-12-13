import json

def restore_all_books(all_books):
    try:
        with open("all_books.json", "r") as f:
            all_books = json.load(f)
    except FileNotFoundError:
        all_books = []
    return all_books
