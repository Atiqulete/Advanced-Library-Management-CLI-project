import save_all_books
from datetime import datetime
import random

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Publishing Year: "))
    price = float(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity: "))

    isbn = random.randint(10000, 99999)
    book_added_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "book_added_at": book_added_at,
        "book_last_updated_at": ""
    }

    all_books.append(book)
    save_all_books.save_all_books(all_books)
    print("Book added successfully!")
    return all_books
