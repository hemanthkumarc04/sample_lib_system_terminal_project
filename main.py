# main.py

from library import add_book, remove_book, search_book, list_books
from database import save_to_file, load_from_file


books = load_from_file()

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. List all Books")
    print("5. Exit")
    choice = input("Choose an option: ")
    return choice

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            
        elif choice == '2':
            title = input("Enter book title to remove: ")
            remove_book(title)
        
        elif choice == '3':
            title = input("Enter book title to search for: ")
            search_book(title)
        
        elif choice == '4':
            list_books()
        
        elif choice == '5':
            save_to_file(books)  
            print("Exiting the system...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()