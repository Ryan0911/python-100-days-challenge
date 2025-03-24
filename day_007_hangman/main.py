 # pylint: disable=C0114
import sys
from hangman import HangmanGame, GameState
from utils.data_processor import load_word_list

FILE_PATH = sys.argv[1] if len(sys.argv) > 1 else None

if FILE_PATH:
    word_list = load_word_list(FILE_PATH)
else:
    word_list = ["python", "java", "kotlin", "javascript", "swift", "dart"]

game = HangmanGame(word_list)

while game.get_game_state() == GameState.CONTINUE:

    print(f"Word to guess: {game.get_progress()}")
    guess = input("Guess a letter: ").lower()

    if game.make_a_guess(guess):
        game.display_hangman()
        game.display_lives()

if game.get_game_state() == GameState.WIN:
    print('*' * 20 + "Congratulation, You Win!" + '*' * 20)
else:
    print('*' * 20 + "Game Over!" + '*' * 20)

print(f"The correct word was: {game.get_chosen_word()}")
