class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")

class FictionBook(Book):
    def __init__(self, title, author, isbn, genre):
        super().__init__(title, author, isbn)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

# Skapa instanser av FictionBook och NonFictionBook
fiction_book = FictionBook("The Hobbit", "J.R.R. Tolkien", "978-0547928227", "Fantasy")
nonfiction_book = NonFictionBook("Sapiens", "Yuval Noah Harari", "978-0062316097", "History")

# Använd display_info-metoden för att visa informationen för varje bok
fiction_book.display_info()
print()
nonfiction_book.display_info()
