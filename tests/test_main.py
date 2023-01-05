""" This file includes the tests for the main file """
from unittest import TestCase

from logipass.main import password_gen


class TestPasswordGen(TestCase):
    """
    This class contains the test cases of the function
    password_gen
    """
    def test_length_of_password(self):
        """
        This tests if the length of the password
        is of the same value as user input
        """
        test_pass = password_gen(password_length=12)
        self.assertTrue(len(test_pass), 10)
        self.assertTrue(type(test_pass), str)

    def test_filter_char_password(self):
        """
        This tests if the char specified by the user
        is filtered and not generated in the generated
        password
        """
        test_pass = password_gen(remove=["a"], password_length=20)
        self.assertNotIn("a", test_pass)

    def test_assertion_password(self):
        """
        This tests if the assertion errors are raised when
        the input of the arguments are not of desired type
        """
        with self.assertRaises(AssertionError):
            password_gen(remove={"a": 2})
            password_gen(password_length="a")
