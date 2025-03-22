# pylint: disable=C0301, C0114, W0621

import random

def get_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generates a random password containing a specified number of letters, symbols, and numbers.

    Args:
        nr_letters (int): The number of letters in the password.
        nr_symbols (int): The number of symbols in the password.
        nr_numbers (int): The number of numbers in the password.

    Returns:
        str: A randomly generated password with the specified composition.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = random.choices(population=letters, k=nr_letters) + \
                    random.choices(population=numbers, k=nr_numbers) + \
                    random.choices(population=symbols, k=nr_symbols)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
