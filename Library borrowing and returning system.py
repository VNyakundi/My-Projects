class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Book is available by default

    def __str__(self):
        return f"'{self.title}' by {self.author} {'(Available)' if self.is_available else '(Borrowed)'}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # A list to store Book objects
        self.borrowed_books = {}  # Tracks borrowed books and their borrowers

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(book)

    def borrow_book(self, book_title, borrower):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.is_available:
                    book.is_available = False
                    self.borrowed_books[book.title] = borrower
                    print(f"{borrower} borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Sorry, no book titled '{book_title}' is available in the library.")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            borrower = self.borrowed_books.pop(book_title)
            for book in self.books:
                if book.title == book_title:
                    book.is_available = True
                    print(f"'{book.title}' returned by {borrower}.")
                    return
        print(f"No record of borrowing for the book '{book_title}'.")

# Example usage
library = Library("City Library")

# Add books to the library
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Display books
library.display_books()

# Borrow a book
library.borrow_book("1984", "Alice")
library.borrow_book("1984", "Bob")  # Try borrowing it again

# Display books after borrowing
library.display_books()

# Return a book
library.return_book("1984")

# Display books after returning
library.display_books()
