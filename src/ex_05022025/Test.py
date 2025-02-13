import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])
def test_login(username, password):
    print(f"Testing login with {username} and {password}")
    assert username and password  # Dummy assertion

import unittest

class TestLogin(unittest.TestCase):
    def test_login(self):
        data = [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3")]
        for username, password in data:
            with self.subTest(username=username, password=password):
                print(f"Testing login with {username} and {password}")
                self.assertTrue(username and password)

if __name__ == "__main__":
    unittest.main()
