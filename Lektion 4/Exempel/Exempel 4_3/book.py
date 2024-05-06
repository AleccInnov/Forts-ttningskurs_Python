class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.is_available:
            self.books_borrowed.append(book)
            book.is_available = False
            print(f"{self.name} borrowed '{book.title}' by {book.author}.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.is_available = True
            print(f"{self.name} returned '{book.title}' by {book.author}.")
        else:
            print(f"Error: '{book.title}' was not borrowed by {self.name}.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_info()
            print()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
