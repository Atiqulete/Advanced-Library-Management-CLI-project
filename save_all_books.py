import json

def save_all_books(all_books):
    with open("all_books.json", "w") as f:
        json.dump(all_books, f, indent=4)
