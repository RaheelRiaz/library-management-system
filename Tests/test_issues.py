import unittest
from data_store import library, members, issues
from book import Book
from member import Member
from issue_return import IssueRecord, issue_book, return_book

class TestIssues(unittest.TestCase):
    def setUp(self):
        library.books.clear()
        members.clear()
        issues.clear()

        # Seed sample data
        library.add_book(Book('111', 'Python 101', 'Guido', 5))
        library.add_book(Book('222', 'Flask Web Dev', 'Miguel', 2))
        members['1'] = Member('1', 'Alice')
        members['2'] = Member('2', 'Bob')

    def test_issue_book_success(self):
        mem = members['1']
        ok = issue_book(library, "111", mem) 
        self.assertTrue(ok)
        if ok:
            issues.append(IssueRecord(mem.member_id, "111", library.books["111"].title))
        self.assertEqual(len(issues), 1)
        self.assertEqual(library.books.get("111").copies, 4)

    def test_issue_book_no_copies(self):
        mem1 = members['1']
        mem2 = members['2']
        issue_book(library, "222", mem1)
        issue_book(library, "222", mem1)
        ok = issue_book(library, "222", mem2)
        self.assertFalse(ok)

    def test_return_book_success(self):
        mem = members['1']
        issue_book(library, "111", mem)
        ok = return_book(library, "111", mem)
        self.assertTrue(ok)
        for r in issues:
                if r.member_id == "1" and r.isbn == "111":
                    issues.remove(r)
                    break
        self.assertEqual(len(issues), 0)
        self.assertEqual(library.books.get("111").copies, 5)

    def test_return_book_not_issued(self):
        mem = members['1']
        ok = return_book(library, "999", mem)
        self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()