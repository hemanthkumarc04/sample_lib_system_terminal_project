# library.py

books = []

def add_book(title, author):
    """Add a book to the library."""
    book = {'title': title, 'author': author}
    books.append(book)
    print(f'Book "{title}" added to the library.')

def remove_book(title):
    """Remove a book from the library by its title."""
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            print(f'Book "{title}" removed from the library.')
            return
    print(f'Book "{title}" not found.')

def search_book(title):
    """Search for a book by its title."""
    for book in books:
        if book['title'].lower() == title.lower():
            print(f'Found book: {book["title"]} by {book["author"]}')
            return
    print(f'Book "{title}" not found.')

def list_books():
    """List all books in the library."""
    if not books:
        print("No books in the library.")
        return
    print("Books in the library:")
    for book in books:
        print(f'- {book["title"]} by {book["author"]}')