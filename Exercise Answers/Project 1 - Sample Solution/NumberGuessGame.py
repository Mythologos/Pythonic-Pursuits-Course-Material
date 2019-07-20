# The following will contain two functions.
# The first will be a number-guessing game in which an integer is supplied as an argument.
# Then, the game starts and proceeds until the correct integer is guessed.
# The program reports back on each input whether it is above or below the target number.
# The second will be the same as the first, but will take an upper value which will determine the range of guessing.
# This value will be obtained during runtime.

import random


def known_hc():
    # type: () -> None
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


def unknown_hc():
    # type: () -> None
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


def introduction():
    print("Welcome to the Number-Guess Menu.")
    print("There are two variants available for the Number Guessing Game.")
    print("The Known variant requires you to supply a number that is the answer at the beginning.")
    print("It is useful for testing purposes.")
    print("The Unknown variant requires you to supply an upper limit and randomly chooses a value to be sought.")
    help_message()


def help_message():
    print("To select a game, please type Known or Unknown. To quit, type Quit.")
    print("To repeat your options, type Help.")


def main_menu():
    # type: () -> None
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
