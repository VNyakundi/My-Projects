# Library MMS system using OOP


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_details(self):
        """Display details of the book."""
        print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")

    def borrow(self):
        """Reduce the number of available copies when a book is borrowed."""
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_book(self):
        """Increase the number of available copies when a book is returned."""
        self.copies += 1


# Class: Person (Base Class)
class Person:
    def __init__(self, name):
        self.name = name


# Class: Admin
class Admin(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library

    def add_book(self, title, author, copies):
        """Add a book to the library."""
        self.library.add_book(Book(title, author, copies))
        print(f"Book '{title}' by {author} added with {copies} copies.")

    def remove_book(self, title):
        """Remove a book from the library."""
        if self.library.remove_book(title):
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' not found in the library.")


# Class: User
class User(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library
        self.borrowed_books = []

    def borrow_book(self, title):
        """Borrow a book from the library."""
        book = self.library.find_book(title)
        if book and book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{title}'.")
        else:
            print(f"'{title}' is not available.")

    def return_book(self, title):
        """Return a borrowed book to the library."""
        for book in self.borrowed_books:
            if book.title == title:
                book.return_book()
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{title}'.")
                return
        print(f"{self.name} does not have the book '{title}'.")

    def view_borrowed_books(self):
        """Display all borrowed books."""
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")


# Class: Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def remove_book(self, title):
        """Remove a book from the library."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        """Display all books in the library."""
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                book.display_details()
        else:
            print("No books available in the library.")


# Testing the Library Management System
if __name__ == "__main__":
    # Create a Library instance
    library = Library()

    # Create an Admin
    admin = Admin("Alice", library)

    # Admin adds books to the library
    admin.add_book("Python Programming", "John Doe", 5)
    admin.add_book("Data Structures", "Jane Smith", 3)

    # Create a User
    user = User("Bob", library)

    # Display books in the library
    print("\nLibrary Books:")
    library.display_books()

    # User borrows books
    print("\nBorrowing Books:")
    user.borrow_book("Python Programming")
    user.borrow_book("Data Structures")
    user.borrow_book("Python Programming")  # Borrowing the same book again

    # View borrowed books
    print("\nUser's Borrowed Books:")
    user.view_borrowed_books()

    # User returns a book
    print("\nReturning Books:")
    user.return_book("Python Programming")

    # Display books in the library after return
    print("\nLibrary Books After Return:")
    library.display_books()
