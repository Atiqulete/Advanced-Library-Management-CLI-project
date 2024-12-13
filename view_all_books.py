def view_all_books(all_books):
    if not all_books:
        print("No books available.")
        return
    for book in all_books:
        print("\n--- Book Details ---")
        for key, value in book.items():
            print(f"{key.capitalize()}: {value}")
