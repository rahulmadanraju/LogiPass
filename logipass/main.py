""" This file includes functions of the password generation. """

from random import choices
import string
from typing import List

SPECIALS = "~!@#$%^&*()_-+={[}]|:<,>.?/"

ALL_PASS_CHARS = string.ascii_letters + string.digits + SPECIALS


def password_gen(*, letters: bool = False, numbers: bool = False,
                 special_chars: bool = False,
                 password_length: int = 8):  # remove: List[str] = None,
    """
    This function generates the password when called. It also contains the
    feature to provide the password containing chars based on user provided
    length and also to remove/filter certain chars if not required
    in the password.
    Args:
     - remove: filter the not required chars from password
     - password_length: provide the length of the password

    Returns:
        password as per the user requirement
    """

    if letters and numbers and special_chars:
        password = "".join(choices(ALL_PASS_CHARS, k=password_length))

    elif letters and numbers:
        password = "".join(
            choices(string.ascii_letters + string.digits, k=password_length))

    elif numbers and special_chars:
        password = "".join(
            choices(string.digits + SPECIALS, k=password_length))

    elif letters and special_chars:
        password = "".join(
            choices(string.ascii_letters + SPECIALS, k=password_length))

    elif special_chars:
        password = "".join(choices(SPECIALS, k=password_length))

    elif numbers:
        password = "".join(choices(string.digits, k=password_length))

    elif letters:
        password = "".join(choices(string.ascii_letters, k=password_length))

    else:
        password = "".join(choices(ALL_PASS_CHARS, k=password_length))

    return password
    '''assert isinstance(remove, list) or remove is None, (
            f"Not of a required type 'List' " f"instead it is '{type(
            remove)}'."
        )
        assert isinstance(password_length, int), (
            f"Not of a required type 'int' instead it " f"is '{type(remove)}'."
        )'''

    '''if remove:
        filtered_pass = str([ALL_PASS_CHARS.replace(i, "") for i in remove])
        return "".join(choices(filtered_pass, k=password_length))

    return "".join(choices(ALL_PASS_CHARS, k=password_length))'''


if __name__ == "__main__":
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=True, special_chars=False)}")
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=False, special_chars=True)}")
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=True, special_chars=True)}")
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=False, special_chars=True)}")
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=True, special_chars=False)}")
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=False, special_chars=False)}")
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=True, special_chars=True)}")
