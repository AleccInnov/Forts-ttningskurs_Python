from book import FictionBook, NonFictionBook, User, Library

# Skapa några böcker
book1 = FictionBook("The Hobbit", "J.R.R. Tolkien", "978-0547928227", "Fantasy")
book2 = NonFictionBook("Sapiens", "Yuval Noah Harari", "978-0062316097", "History")
book3 = FictionBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-0747532743", "Fantasy")

# Skapa en användare
user1 = User("Alice", "alice@email.com")

# Skapa en biblioteksinventering
library = Library()

# Lägg till böckerna i biblioteket
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Visa alla böcker i biblioteket
library.display_books()

# Låna en bok
user1.borrow_book(book1)

# Försök att låna samma bok igen (boken är inte tillgänglig)
user1.borrow_book(book1)

# Återlämna boken
user1.return_book(book1)

# Visa alla böcker igen för att se ändringen i tillgänglighet
library.display_books()
