import add_books
import view_all_books
import restore_books_file
import update_book
import delete_book
import lend_books
import return_books
import json

all_books = []  
borrowed_books = [] 

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")
    print("6. Return Book")

    
    all_books = restore_books_file.restore_all_books(all_books)
    try:
        with open("borrowed_books.json", "r") as f:
            content = f.read().strip()
            if content:
                borrowed_books = json.loads(content)
            else:
                borrowed_books = []
    except FileNotFoundError:
        borrowed_books = []

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_book.update_books(all_books)
    elif menu == "4":
        all_books = delete_book.delete_books(all_books)
    elif menu == "5":
        all_books, borrowed_books = lend_books.lend_book(all_books, borrowed_books)
    elif menu == "6":
        all_books, borrowed_books = return_books.return_book(all_books, borrowed_books)
    else:
        print("Choose a valid number.")
