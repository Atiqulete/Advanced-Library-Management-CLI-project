import json
from datetime import datetime
import save_all_books

def return_book(all_books, borrowed_books):
    borrower_name = input("Enter Borrower's Name: ")
    book_title = input("Enter Book Title to Return: ")

    for borrowed_book in borrowed_books:
        if borrowed_book["title"].lower() == book_title.lower() and borrowed_book["borrower_name"].lower() == borrower_name.lower():
            borrowed_books.remove(borrowed_book)

            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    book["book_last_updated_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    save_all_books.save_all_books(all_books)
                    break

            with open("borrowed_books.json", "w") as f:
                json.dump(borrowed_books, f, indent=4)
            print(f"Book '{book_title}' returned successfully!")
            return all_books, borrowed_books
    print("Book or Borrower not found.")
    return all_books, borrowed_books
