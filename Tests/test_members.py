import unittest
from data_store import members
from member import Member

class TestMembers(unittest.TestCase):
    def setUp(self):
        members.clear()

        members['1'] = Member('1', 'Alice')
        members['2'] = Member('2', 'Bob')

    def test_add_member(self):
        members['3'] = Member('3', 'Charlie')
        self.assertIn('3', members)

    def test_edit_member(self):
        members['1'].name = "Alice Updated"
        self.assertEqual(members['1'].name, "Alice Updated")

    def test_delete_member(self):
        del members['2']
        self.assertNotIn('2', members)

if __name__ == "__main__":
    unittest.main()