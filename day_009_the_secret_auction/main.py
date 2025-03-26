# pylint: disable=C0103, C0113, C0114, C0301
import os
from utils.art import ArtHelper
art_helper = ArtHelper()
print(art_helper.secret_auction())

continue_or_not = "yes"
max_name = ""
max_bid = 0
bids = {}

while continue_or_not == "yes":
    name = input("what is your name?: ").strip()
    bid = -1
    while bid <= 0:
        try:
            bid = float(input("What is your bid?: $").strip())
            if bid <= 0:
                print("Bid must be greater than 0. Please enter a valid bid.")
        except ValueError:
            print("Invalid input. Please enter a valid bid.")

    if bid > max_bid:
        max_bid = bid
        max_name = name
    bids[name] = bid

    continue_or_not = input("Are there any other bidders? Type 'yes' to continue. Otherwise, type any key to exit.\n").strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear')

print("Bids received:")
for name, bid in bids.items():
    print(f"{name}: ${bid}")
print('-' * 20)
print(f"The winner is {max_name} with a bid of ${max_bid}.")
