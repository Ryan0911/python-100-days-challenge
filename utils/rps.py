# pylint: disable=C0114, R0903
import random
from enum import IntEnum

class Choice(IntEnum):
    """Enumeration for RPS game choices"""
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Result(IntEnum):
    """Enumeration for RPS game results"""
    DRAW = 0
    COMPUTER_WINS = 1
    PLAYER_WINS = 2

class RpsGame:
    """
    This is Rock Scissor Paper Game between player and computer
    Using to play game and record the result.
    """
    def __init__(self):
        pass

    def __make_choice(self):
        """Generate a random choice for the computer."""
        return random.choice(list(Choice))

    def get_game_result(self, player_choice):
        """
        Get the game result between player and computer.
        
        Args:
            player_choice (int): Player's selection (0=rock, 1=paper, 2=scissors)
            
         Returns:
            tuple: (result, computer_choice) where:
                - result: 0 if draw, 1 if computer wins, 2 if player wins
                - computer_choice: The computer's selection (0=rock, 1=paper, 2=scissors)
        """
        computer_choice = self.__make_choice()

        if player_choice == computer_choice:
            return Result.DRAW, computer_choice

        computer_wins = [
            (Choice.ROCK, Choice.SCISSORS),
            (Choice.PAPER, Choice.ROCK),
            (Choice.SCISSORS, Choice.PAPER)
        ]

        if (computer_choice, player_choice) in computer_wins:
            return Result.COMPUTER_WINS, computer_choice

        return Result.PLAYER_WINS, computer_choice
