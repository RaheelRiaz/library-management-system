import unittest
from data_store import library
from book import Book
from search import search_by_title, search_by_author, search_by_isbn

class TestSearch(unittest.TestCase):
    def setUp(self):
        library.books.clear()

        library.add_book(Book('111', 'Python 101', 'Guido', 5))
        library.add_book(Book('222', 'Flask Web Dev', 'Miguel', 2))

    def test_search_by_title(self):
        results = search_by_title(library, "Python")
        self.assertTrue(any("Python" in b.title for b in results))

    def test_search_by_author(self):
        results = search_by_author(library, "Miguel")
        self.assertEqual(results[0].author, "Miguel")

    def test_search_by_isbn(self):
        b = search_by_isbn(library, "111")
        self.assertIsNotNone(b)
        self.assertEqual(b.title, "Python 101")

if __name__ == "__main__":
    unittest.main()