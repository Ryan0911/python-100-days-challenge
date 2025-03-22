# pylint: disable=C0114, C0301
import unittest
from utils.generator import get_password

class TestPasswordMethods(unittest.TestCase):
    """Unit tests for the get_password function."""

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def setUp(self):
        """Set up test case parameters and generate a test password."""
        self.nr_letters = 8
        self.nr_symbols = 3
        self.nr_numbers = 4
        self.password = get_password(self.nr_letters, self.nr_symbols, self.nr_numbers)

    def test_total_length(self):
        """Test that the generated password has the expected total length."""
        self.assertEqual(len(self.password), self.nr_letters + self.nr_numbers + self.nr_symbols)

    def test_letters(self):
        """Test that the generated password contains the expected number of letters."""
        letter_count = sum(1 for char in self.password if char in self.letters)
        self.assertEqual(letter_count, self.nr_letters)

    def test_numbers(self):
        """Test that the generated password contains the expected number of numbers."""
        numbers_count = sum(1 for char in self.password if char in self.numbers)
        self.assertEqual(numbers_count, self.nr_numbers)

    def test_symbols(self):
        """Test that the generated password contains the expected number of symbols."""
        symbols_count = sum(1 for char in self.password if char in self.symbols)
        self.assertEqual(symbols_count, self.nr_symbols)

    def test_incorrect_parameters(self):
        """
        Test case with incorrect parameters to verify error handling.

        This test intentionally provides incorrect values to `get_password`
        and ensures that the resulting password does not meet expected criteria.
        """
        error_password = get_password(self.nr_letters, self.nr_letters, self.nr_letters)
        self.assertNotEqual(len(error_password), self.nr_letters + self.nr_symbols + self.nr_numbers)

        letter_count = sum(1 for char in error_password if char in self.letters)
        self.assertEqual(letter_count, self.nr_letters)

        symbols_count = sum(1 for char in error_password if char in self.symbols)
        self.assertNotEqual(symbols_count, self.nr_symbols)

        numbers_count = sum(1 for char in error_password if char in self.numbers)
        self.assertNotEqual(numbers_count, self.nr_numbers)

if __name__ == '__main__':
    unittest.main(verbosity=2)
