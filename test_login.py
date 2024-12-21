import unittest

def login(username, password):
    correct_username = "123abc"
    correct_password = "password123"
    
    return username == correct_username and password == correct_password

class TestLogin(unittest.TestCase):

    def test_login_success(self):
        self.assertTrue(login("123abc", "password123"))
    
    def test_invalid_username(self):
        self.assertFalse(login("wronguser", "password123"))
    
    def test_invalid_password(self):
        self.assertFalse(login("123abc", "wrongpassword"))

if __name__ == "__main__":
    unittest.main()