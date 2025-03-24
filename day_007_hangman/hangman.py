# pylint: disable=C0114
import random
from enum import Enum
from utils.art import ArtHelper

art_helper = ArtHelper()

class GameState(Enum):
    """An enumeration of possible game states."""    
    CONTINUE = 1
    LOSE = 0
    WIN = 2

class HangmanGame:
    """A simple Hangman game implementation in Python.

    Attributes:
        chosen_word (str): The word to be guessed.
        lives (int): Number of remaining lives.
        stages (list): ASCII art representations of the Hangman stages.
        progress (list): The current guessed state of the word.
        win (bool): Whether the player has won the game.
        guessed_letters (list): List of guessed letters.
    """
    def __init__(self, word_list):
        self.chosen_word = random.choice(word_list)
        self.lives = 6
        self.stages = art_helper.hangman_stages()
        self.progress = ['_' for x in range(len(self.chosen_word))]
        self.guessed_letters = set()
        art_helper.hangman_start()

    def display_progress(self):
        """Display the current progress of the game."""
        print(''.join(self.progress))

    def display_hangman(self):
        """Display the current state of the Hangman."""
        print(self.stages[6 - self.lives])

    def display_lives(self):
        """Display the number of remaining lives."""
        print('*' * 20 + f"{self.lives}/6 LIVES LEFT" + '*' * 20)

    def make_a_guess(self, guess_letter):
        """Make a guess and update the game state.

        Args:
            guess_letter (str): The letter guessed by the player.
        
        Returns:
            bool: Whether the user guess was valid.      
        """
        if len(guess_letter) != 1:
            print("Please enter a single letter.")
            return False
        if not guess_letter.isalpha():
            print("Please enter a valid letter.")
            return False
        if guess_letter in self.guessed_letters:
            print(f"You've already guessed {guess_letter}. Try again.")
            return False

        if guess_letter in self.chosen_word:
            self.progress = [
                letter if letter == guess_letter else progress_letter
                for letter, progress_letter in zip(self.chosen_word, self.progress)
            ]
        else:
            self.lives -= 1
        self.guessed_letters.add(guess_letter)
        self.display_progress()
        return True

    def get_game_state(self):
        """Check and return the current game state.

        Returns:
            GameState: The current game state (CONTINUE, LOSE, WIN).
        """
        if self.lives == 0:
            return GameState.LOSE
        if '_' not in self.progress:
            return GameState.WIN
        return GameState.CONTINUE

    def get_game_lives(self):
        """Get the current number of remaining lives.
        
        Returns:
            int: current number of lives
        """
        return self.lives
    def get_progress(self):
        """Get the current progress as a string.
        
        Returns:
            str: The current progress of the game.
        """
        return ''.join(self.progress)

    def get_chosen_word(self):
        """Get the chosen word.

        Returns:
            str: The chosen word.
        """
        return self.chosen_word
