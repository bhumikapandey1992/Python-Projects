class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books  # aggregation - books are passed in from outside

    def show_books(self):
        for book in self.books:
            print(f"Book: {book.title}")

    def __del__(self):
        print("Library was deleted.")

book1 = Book("1984")
book2 = Book("To Kill a Mockingbird")

library = Library([book1, book2])
library.show_books()

del library
print(book1.title) 
print(book2.title) 
