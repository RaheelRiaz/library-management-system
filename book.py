class Book:
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies
    def __repr__(self):
        return f"<Book {self.title} ({self.isbn}) copies={self.copies}>"
