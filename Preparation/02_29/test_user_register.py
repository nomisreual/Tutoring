import unittest

# Class modelling our user:


class User:
    def __init__(self, username, password="1234"):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

# "Database" with unique constraint on username:


class UserRegistry:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        if user.username in self.users.keys():
            raise Exception
        else:
            self.users[user.username] = user.password


class TestUserRegistry(unittest.TestCase):
    def test_registration_success(self):
        user_registry = UserRegistry()
        user_registry.add_user(User(username="Pete"))
        self.assertEqual(len(user_registry.users),
                         1,
                         "Should be one user in the database")


if __name__ == "__main__":
    unittest.main()
