import save_all_books
from datetime import datetime

def update_books(all_books):
    search_title = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"].lower() == search_title.lower():
            book["title"] = input("Enter New Title: ")
            book["author"] = input("Enter New Author: ")
            book["year"] = int(input("Enter New Publishing Year: "))
            book["price"] = float(input("Enter New Price: "))
            book["quantity"] = int(input("Enter New Quantity: "))
            book["book_last_updated_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            save_all_books.save_all_books(all_books)
            print("Book updated successfully!")
            return all_books
    print("Book not found.")
    return all_books
