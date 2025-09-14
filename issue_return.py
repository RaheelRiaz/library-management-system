class IssueRecord:
    def __init__(self, member_id, isbn, title):
        self.member_id = member_id
        self.isbn = isbn
        self.title = title
def issue_book(library, isbn, member):
    if isbn in library.books and library.books[isbn].copies > 0:
        library.books[isbn].copies -= 1
        member.borrowed_books.append(isbn)
        return True
    return False
def return_book(library, isbn, member):
    if isbn in member.borrowed_books:
        member.borrowed_books.remove(isbn)
        if isbn in library.books:
            library.books[isbn].copies += 1
        return True
    return False
