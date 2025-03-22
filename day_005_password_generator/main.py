# pylint: disable=C0114
from utils.generator import get_password

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

PASSWORD = get_password(nr_letters, nr_symbols, nr_numbers)
print(f"Your password is: {PASSWORD}")
