import save_all_books

def delete_books(all_books):
    search_title = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"].lower() == search_title.lower():
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book deleted successfully!")
            return all_books
    print("Book not found.")
    return all_books
