from book import Book, User, Library

# Skapa några böcker
book1 = Book("Python Programming", "John Doe", "978-1234567890")
book2 = Book("Data Structures", "Jane Smith", "978-0987654321")

# Skapa en användare och bibliotek
user1 = User("Alice", "alice@email.com")
library = Library()

# Lägg till böckerna i biblioteket
library.add_book(book1)
library.add_book(book2)

# Visa alla böcker i biblioteket
library.display_books()

# Låna en bok
user1.borrow_book(book1)

# Visa alla böcker igen för att se ändringen i tillgänglighet
library.display_books()

# Försök att låna samma bok igen
user1.borrow_book(book1)

# Återlämna boken
user1.return_book(book1)

# Visa alla böcker igen för att se ändringen i tillgänglighet
library.display_books()
