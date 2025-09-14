import unittest
from data_store import library
from book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        library.books.clear()

        library.add_book(Book('111', 'Python 101', 'Guido', 5))
        library.add_book(Book('222', 'Flask Web Dev', 'Miguel', 2))

    def test_add_book(self):
        library.add_book(Book('333', 'Django Guide', 'Adrian', 3))
        self.assertIsNotNone(library.books.get('333'))

    def test_edit_book(self):
        b = library.books.get('111')
        b.title = "Python Basics"
        self.assertEqual(library.books.get('111').title, "Python Basics")

    def test_delete_book(self):
        library.remove_book('222')
        self.assertIsNone(library.books.get('222'))

if __name__ == "__main__":
    unittest.main()