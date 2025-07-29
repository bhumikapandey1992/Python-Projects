# Class method - A class method is a method that belongs to the class, not the instance of the class.
#              - define it using the @classmethod decorator,
#              - it always takes cls as the first parameter — instead of self

# ALTERNATIVE CONSTRUCTOR/FACTORY METHOD

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_string(cls, book_str):
        title, author, pages = book_str.split(";")
        return cls(title, author, int(pages))

book = Book.from_string('The Hobbit;J.R.R. Tolkien;310')
print(f"Title: {book.title}, Author: {book.author}, Pages: {book.pages}")

