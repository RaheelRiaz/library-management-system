import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("12345", "Test Title", "John Doe", 3)

    def test_initialization(self):
        self.assertEqual(self.book.isbn, "12345")
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.copies, 3)

    def test_repr(self):
        expected = "<Book Test Title (12345) copies=3>"
        self.assertEqual(repr(self.book), expected)

    def test_update_copies(self):
        self.book.copies = 5
        self.assertEqual(self.book.copies, 5)