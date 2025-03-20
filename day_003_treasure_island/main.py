# pylint: disable=C0114, C0301, W0621
import sys
import time
from art import ArtHelper


def take_action(seconds=1, action="Waiting"):
    """Pauses execution for a specified number of seconds while displaying a progress bar.

    Args:
        seconds (int, optional): Number of seconds to wait. Defaults to 1.
        action (str, optional): Action displayed with progress bar. Defaults to "Waiting".
    """     
    for i in range(seconds):
        progress = "#" * (i + 1) + "-" * (seconds - i - 1)
        print(f"\r{action}: [{progress}] {i + 1}/{seconds} sec", end="", flush=True)
        time.sleep(1)
    print()

def game_over(message):
    """Handles game-over scenarios by displaying a message and terminating the program.

    Args:
        message (str): The message to display when the game ends.
    """
    art_generator.game_over()
    print(message)
    sys.exit()

def get_valid_input(prompt, valid_choices):
    """Prompts the user for input and ensures it is valid.

    Args:
        prompt (str): The message displayed to the user.
        valid_choices (set): A set of valid input choices.

    Returns:
        str: A valid user input from the given choices.
    """
    action = ""
    while action not in valid_choices:
        action = input(prompt).strip().lower()
    return action

art_generator = ArtHelper()

art_generator.treasure_start()
print('''Welcome to Treasure Island
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?''')

action = get_valid_input('Type "left" or "right"\n', {"left", "right"})

art_generator.person_walk()
take_action(2, f'Walking to the {action}...')


if action == 'right':
    game_over("You fell into a hole. Game Over.")


print("You've come to a lake. There is an island in the middle of the lake.\n")
action = get_valid_input('Type "wait" to wait for a boat. Type "swim" to swim across\n', {'swim', 'wait'})


if action == 'swim':
    art_generator.person_swimming()
    take_action(2, 'Swimming...')
    art_generator.shark()
    take_action(2, 'Under attacking...')
    game_over("You get attacked by an angry shark. Game Over.")


take_action(2, 'Waiting for the boat...')

art_generator.boat()
take_action(2, 'On boarding...')


art_generator.door_close()
print('''You arrive at the island unharmed. There is a house with 3 doors. 
One red, one yellow and one blue. Which colour do you choose?\n''')

action = get_valid_input('Type "red", "yellow", or "blue"\n', {"red", "yellow", "blue"})

take_action(2, f'Open the {action} door...')
art_generator.door_open()

if action == 'red':
    art_generator.fire()
    take_action(2, 'Burning....')
    game_over("It's a room full of fire. Game Over.")

if action == 'blue':
    art_generator.wolf()
    take_action(2, 'Howling....')
    game_over("You enter a room of wolves. Game Over.")

take_action(2, 'Exploring....')
art_generator.treasure_close()
take_action(2, 'Found the box! Opening the box...')

art_generator.treasure_open()
print('You found the treasure! You Win!')
