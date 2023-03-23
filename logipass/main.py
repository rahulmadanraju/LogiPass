""" This file includes functions of the password generation. """

from random import choices
import string
from typing import List

SPECIALS = "~!@#$%^&*()_-+={[}]|:<,>.?/"

ALL_PASS_CHARS = string.ascii_letters + string.digits + SPECIALS


def password_gen(
    *,
    letters: bool = False,
    numbers: bool = False,
    special_chars: bool = False,
    password_length: int = 8,
):
    """
    This function generates the password when called. It also contains the
    feature to provide the password containing letters, numbers or special
    characters based on user provided input along with a definite length.
    Args:
     - letters: set to True to give letters
     - numbers: set to True to give numbers
     - special_chars: set to True to give special characters
     - password_length: provide the length of the password

    Returns:
        password as per the user requirement
    """

    if letters and numbers and special_chars:
        password = "".join(choices(ALL_PASS_CHARS, k=password_length))

    elif letters and numbers:
        password = "".join(
            choices(string.ascii_letters + string.digits, k=password_length)
        )

    elif numbers and special_chars:
        password = "".join(choices(string.digits + SPECIALS, k=password_length))

    elif letters and special_chars:
        password = "".join(choices(string.ascii_letters + SPECIALS, k=password_length))

    elif special_chars:
        password = "".join(choices(SPECIALS, k=password_length))

    elif numbers:
        password = "".join(choices(string.digits, k=password_length))

    elif letters:
        password = "".join(choices(string.ascii_letters, k=password_length))

    else:
        password = "".join(choices(ALL_PASS_CHARS, k=password_length))

    return password


if __name__ == "__main__":
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=True, special_chars=False)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=False, special_chars=True)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=True, special_chars=True)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=False, special_chars=True)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=False, numbers=True, special_chars=False)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=False, special_chars=False)}"
    )
    print(
        f"Password is: "
        f"{password_gen(letters=True, numbers=True, special_chars=True)}"
    )
