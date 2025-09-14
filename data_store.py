from library import Library
from member import Member
from issue_return import IssueRecord
from book import Book

# In-memory data stores (shared across the app)
library = Library()
members = {}   # member_id -> Member object
issues = []    # list of IssueRecord
user_db = {'admin': 'admin123'}

# -------------------
# Sample Data
# -------------------
library.add_book(Book('9780140449136', 'Meditations', 'Marcus Aurelius', 3))
library.add_book(Book('9781491957660', 'Flask Web Development', 'Miguel Grinberg', 2))

members['1'] = Member('1', 'Alice')
members['2'] = Member('2', 'Bob')

issues.append(IssueRecord("1", "9780140449136", "Meditations"))  # Alice borrowed Meditations