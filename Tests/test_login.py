import unittest
from data_store import user_db
from auth_system import authenticate

class TestLogin(unittest.TestCase):
    def setUp(self):
        user_db.clear()

        user_db['admin'] = 'admin123'

    def test_login_success(self):
        self.assertTrue(authenticate('admin', 'admin123', user_db))

    def test_login_failure(self):
        self.assertFalse(authenticate('admin', 'wrong', user_db))

if __name__ == "__main__":
    unittest.main()