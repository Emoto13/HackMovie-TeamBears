import unittest

from models.user import User
from utils.bootstrap import bootstrap
from gateway.sign_up import add_user_to_database
import os


class DatabaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap()


DatabaseTestCase.setUpClass()


class MyTestCase(unittest.TestCase):
    def test_add_user(self):
        add_user_to_database(User(user_name="Ivan", user_password='alabala'))


if __name__ == '__main__':
    unittest.main()
