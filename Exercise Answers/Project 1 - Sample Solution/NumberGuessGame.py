"""
This program contains code to run two types of number-guessing games.
The first will be a number-guessing game in which an integer is supplied as an argument--
in other words, where the number to be guessed is known.
This game serves to help students to understand the logic of their program and to debug it as needed.
The second will have the user supply an upper limit for a randomization of the number to guess.
In both of the above games, the program reports back on each input whether it is above or
below the target number. Both of these games can be accessed via a menu;
there is also a help command for the game that displays instructions.
"""

import random


def known_hc() -> None:
    """
    This method executes the number-guessing game in which the seek value is known.
    :return: None.
    """
    start_condition: bool = False
    seek_value: int = 0
    while not start_condition:
        sv_input_string: str = input("Please give the seek value: ").strip()
        if not sv_input_string.isdigit():
            print("The given value to be sought is invalid. Please try again.")
        else:
            seek_value = int(sv_input_string)
            start_condition = True
            print("Let the game begin!")
    else:
        win_condition: bool = False
        while not win_condition:
            guessed_value = input("Please supply a new guess: ").strip()
            if not guessed_value.isdigit():
                print("Invalid input. Try again.")
            else:
                guessed_value = int(guessed_value)
                if guessed_value == seek_value:
                    print("That input is correct!")
                    win_condition = True
                else:
                    if guessed_value > seek_value:
                        print("That input is above the value sought.")
                    else:
                        print("That input is below the value sought.")
        print("Congratulations! You won!")


def unknown_hc() -> None:
    """
    This method executes the number-guessing game in which the seek value is unknown.
    Instead, the user may supply the upper limit for teh range of seek values.
    :return: None.
    """
    upper_value: int = 0
    while not upper_value:
        uv_input_string = input("Please supply an upper limit for the game: ").strip()
        if not uv_input_string.isdigit():
            print("The given upper limit for the game is invalid. Please try again.")
        elif uv_input_string.isdigit() and int(uv_input_string) == 0:
            print("The given upper limit is less than or equal to zero. Please choose a higher limit.")
        else:
            upper_value = int(uv_input_string)
            print("Let the game begin!")
    else:
        seek_value: int = random.randint(0, upper_value)
        win_condition: bool = False
        while not win_condition:
            guessed_value = input("Please supply a new guess: ").strip()
            if not guessed_value.isdigit():
                print("Invalid input. Try again.")
            else:
                guessed_value = int(guessed_value)
                if guessed_value == seek_value:
                    print("That input is correct!")
                    win_condition = True
                else:
                    if guessed_value > seek_value:
                        if guessed_value <= upper_value:
                            print("That input is above the value sought.")
                        else:
                            print("That input is above the upper limit of the values searched.")
                    else:
                        if guessed_value >= 0:
                            print("That input is below the value sought.")
                        else:
                            print("That input is below the lower limit of the values searched.")
        print("Congratulations! You won!")


def introduction() -> None:
    """
    This method displays the introduction for the number-guessing game's menu.
    :return: None.
    """
    print("Welcome to the Number-Guess Menu.")
    print("There are two variants available for the Number Guessing Game.")
    print("The Known variant requires you to supply a number that is the answer at the beginning.")
    print("It is useful for testing purposes.")
    print("The Unknown variant requires you to supply an upper limit and randomly chooses a value to be sought.")
    help_message()


def help_message() -> None:
    """
    This method displays a help message for the player so that they know what commands are available.
    :return: None.
    """
    print("To select a game, please type Known or Unknown. To quit, type Quit.")
    print("To repeat your options, type Help.")


def main_menu() -> None:
    """
    This method runs the main menu as the user needs it.
    It allows access to both of the number-guessing games, the help message, and the ability to
    end the program with the commands "known", "unknown", "help", and "quit", respectively.
    :return: None.
    """
    game_condition: bool = True
    while game_condition:
        introduction()
        input_condition: bool = False
        while not input_condition:
            print("")
            new_input: str = input(">> ").lower().strip()
            if new_input == "known":
                known_hc()
                input_condition = True
            elif new_input == "unknown":
                unknown_hc()
                input_condition = True
            elif new_input == "help":
                help_message()
            elif new_input == "quit":
                input_condition = True
                game_condition = False
                print("Goodbye!")
            else:
                print("That input was not recognized. Please try again.")
        else:
            if game_condition:
                print("")
                print("-----------------------------------------------------------------------------------------")
                print("You are back on the main menu.")


main_menu()
