# pylint: disable=C0114, C0301
import sys
from utils.art import ArtHelper
from utils.rps import RpsGame, Choice, Result

art_helper = ArtHelper()
rps_game = RpsGame()

display = {
    Choice.ROCK: art_helper.rock,
    Choice.PAPER: art_helper.paper,
    Choice.SCISSORS: art_helper.scissors
}

try:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
    if player_choice not in [0, 1, 2]:
        raise ValueError("Invalid choice!")
except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

print("You chose:")
display[Choice(player_choice)]()

result, computer_choice = rps_game.get_game_result(Choice(player_choice))

print("Computer chose:")
display[computer_choice]()

if result == Result.DRAW:
    print("DRAW")
elif result == Result.COMPUTER_WINS:
    print("You Lose!")
elif result == Result.PLAYER_WINS:
    print("You Win!")
