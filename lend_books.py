import json
from datetime import datetime
import save_all_books

def lend_book(all_books, borrowed_books):
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone: ")
    book_title = input("Enter Book Title to Lend: ")
    due_date = input("Enter Return Due Date (DD-MM-YYYY): ")

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                borrowed_book = {
                    "title": book_title,
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "borrowed_at": datetime.now().strftime("%d-%m-%Y"),
                    "due_date": due_date
                }
                borrowed_books.append(borrowed_book)
                save_all_books.save_all_books(all_books)
                with open("borrowed_books.json", "w") as f:
                    json.dump(borrowed_books, f, indent=4)
                print(f"Book '{book_title}' lent successfully!")
                return all_books, borrowed_books
            else:
                print("Not enough books available to lend.")
                return all_books, borrowed_books
    print("Book not found.")
    return all_books, borrowed_books
