""" This file includes the tests for the main file """
from unittest import TestCase

from logiapp.main import password_gen


class TestPasswordGen(TestCase):
    def test_length_of_password(self):
        test_pass = password_gen(password_length=12)
        self.assertTrue(len(test_pass), 10)
        self.assertTrue(type(test_pass), str)

    def test_filter_char_password(self):
        test_pass = password_gen(remove=["a"], password_length=20)
        self.assertNotIn("a", test_pass)

    def test_assertion_password(self):
        with self.assertRaises(AssertionError):
            password_gen(remove={"a": 2})
            password_gen(password_length="a")
