import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])
def test_login(username, password):
    print(f"Testing login with {username} and {password}")
    assert username and password  # Dummy assertion
