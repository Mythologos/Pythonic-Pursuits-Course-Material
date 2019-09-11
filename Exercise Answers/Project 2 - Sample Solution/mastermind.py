"""
The following composes a game of Mastermind in an enumeration (MMColor) and a class (Mastermind).
Currently, the game automatically runs upon the creation of a Mastermind object.
As of this time, the Mastermind game allows for customization in the number of colors, code slots,
and rounds that the game can have.

This is used as a project in Pythonic Pursuits. The following is a sample solution.
Of the below classes, MMColor will likely be given to students for their use as they please.
The primary objective for them will be to compose the Mastermind game itself in a class.
It is not expected that they will use decorators (e.g. @staticmethod) or dunders (__members__)
besides __init__. However, the code is expected to have some knowledge in the following subjects:
lists, complex conditionals, types of iteration, membership, importing libraries, and classes.
"""

import time
import random
import copy
from aenum import Enum


class MMColor(Enum, init='value full_name'):
    """
    This enumeration correlates color abbreviations, color names, and color integers.
    The Mastermind game utilizes these colors and their abbreviations in its game.
    Except in terms of the instructions and the altered number of possible colors,
    adding or removing colors from this list should not impact the functionality of the game.
    """
    R = (1, "Red")
    B = (2, "Blue")
    Y = (3, "Yellow")
    G = (4, "Green")
    O = (5, "Orange")
    V = (6, "Violet")
    W = (7, "White")
    K = (8, "Black")
    E = (9, "Grey")
    I = (10, "Indigo")
    P = (11, "Pink")
    N = (12, "Brown")

    def __str__(self):
        """
        This method, like __repr__, retrieves a printable version of an MMColor.
        :return: str
        """
        return self.full_name + " (" + self.name + ")"

    def __repr__(self):
        """
        This method, like __str__, retrieves a printable version of an MMColor.
        :return: str
        """
        return self.full_name + " (" + self.name + ")"


class Mastermind:
    """
    This class composes the Mastermind game. It includes its own menu, instructions, and setup.
    """
    def __init__(self) -> None:
        """
        This method establishes and initiates items necessary for the Mastermind game:
        the solution to each round of the game,
        the storage for the user's actions during the game as a reference,
        and the game's introduction and menu.
        """
        self.solution: list = []
        self.memory: list = []
        self.general_introduction()
        self.main_menu()

    def main_menu(self) -> None:
        """
        This method initiates the game's main menu.
        Three commands can be chosen from it:
        a "play" command to set up and start the game,
        a "help" command to retrieve instructions on the game,
        and a "quit" command to end the program.
        :return: None.
        """
        game_condition: bool = True
        while game_condition:
            user_input: str = input(">> ").lower().strip()
            if user_input == 'play':
                num_rounds: str = input("Please give the number of rounds for the game: ")
                if num_rounds.isdigit() and int(num_rounds) > 0:
                    num_rounds: int = int(num_rounds)
                    num_code_slots: str = input("Please give the number of entries in the code: ")
                    if num_code_slots.isdigit() and int(num_code_slots) > 0:
                        num_code_slots: int = int(num_code_slots)
                        num_colors: str = input("Please give the number of colors used: ")
                        if num_colors.isdigit() and num_code_slots <= int(num_colors) <= len(MMColor.__members__):
                            num_colors: int = int(num_colors)
                            self.initialize_mastermind(num_rounds, num_code_slots, num_colors)
                        else:
                            print("That input is invalid. Please try again.")
                            print("You have been returned to the main menu.")
                    else:
                        print("That input is invalid. Please try again.")
                        print("You have been returned to the main menu.")
                else:
                    print("That input is invalid. Please try again.")
                    print("You have been returned to the main menu.")
            elif user_input == 'help':
                self.help_menu()
            elif user_input == 'quit':
                print("Goodbye!")
                game_condition = False
            else:
                print("Input not recognized. Please try again.")
        time.sleep(3)

    @staticmethod
    def general_introduction():
        """
        This method displays the introduction to the Mastermind game.
        :return: None.
        """
        print("Welcome to Mastermind! You are on the main menu.")
        print("Type 'play' to start the game.")
        print("Type 'help' to bring up the help menu, which will describe the game.")
        print("Type 'quit' to leave this interface.")
        print("")

    @staticmethod
    def help_menu():
        """
        This method initiates the Mastermind game's help menu.
        It has the options of "mastermind", which gives a full explanation of the game,
        "commands", which displays the commands and sub-commands of each option in the game,
        and "back", which returns to the main menu.
        :return: None.
        """
        help_condition: bool = True
        print("Would you like to hear about the game Mastermind or the game's commands?")
        print("Type 'mastermind' for the former and 'commands' for the latter.")
        print("Type 'back' to go back.")
        while help_condition:
            help_input: str = input(">> ").lower().strip()
            if help_input in ["mastermind", "commands", "back"]:
                if help_input == "mastermind":
                    print("The game of Mastermind works as follows.")
                    print("The goal of the game is for the player to determine a code.")
                    print("This code is randomized by the game at its beginning.")
                    print("In each round, the player guesses a code of a certain length.")
                    print("The player does so by putting in a letter representing a color in the code,")
                    print("supplying a space after that letter, and then another letter up until the last one.")
                    input("Press enter to continue. (1/5)")
                    print("Then, based on this input, the program determines two facts about the code.")
                    print("First, it determines how many colors are present and in the right place.")
                    print("Second, it determines how many colors are present but not in the right place.")
                    print("It informs the user of how well his or her code does based on these criteria.")
                    input("Press enter to continue. (2/5)")
                    print("Then, the user can guess again. Depending on the user's initial inputs,")
                    print("the user will have a set number of tries to get the code right.")
                    print("The user will be able to see past results and inputs along the way.")
                    print("If the user fails to get the code correct within a limited number of tries,")
                    print("he or she loses. If the user gets the code exactly right, he or she wins.")
                    input("Press enter to continue. (3/5)")
                    print("The colors and their representations in this game are as follows.")
                    print("Red is R. Blue is B. Yellow is Y. Green is G. Orange is O. Violet is V.")
                    print("White is W. Black is K. Grey is E. Indigo is I. Pink is P. Brown is N.")
                    print("The default setting for the game is ten rounds with six colors and four code slots.")
                    print("The colors being used can be checked by typing 'colors' during the game.")
                    input("Press enter to continue. (4/5)")
                    print("Upon starting the game, you will be prompted to give three inputs.")
                    print("First, you will be asked about the number of rounds you have to guess the correct input.")
                    print("The minimum for this is one. Second, you will be asked about the number of code entries.")
                    print("The minimum for this is also one. Third, you will be asked about the number colors.")
                    print("The minimum for this is the number of code entries. The maximum is twelve.")
                    input("Press enter to continue. (5/5)")
                    print("")
                elif help_input == "commands":
                    print("On the main menu, commands are 'help', 'quit', and 'play'.")
                    print("In the game, commands are 'colors' and 'memory'.")
                    print("Under the 'help' command, the 'mastermind' and 'commands' commands are available.")
                    print("")
                else:
                    help_condition = False
                    input("Going back to the main menu... (Press enter to continue.)")
                    time.sleep(3)
                    print("You are now back on the main menu.")
                    print("")
            else:
                print("That input was invalid. Please try again.")

    def initialize_mastermind(self, num_rounds: int, num_code_slots: int, num_colors: int) -> None:
        """
        This method begins the Mastermind game.
        It assures that the solution and memory lists are clear.
        Then, it sets up the game according to the preferences dictated in the game's setup.
        :param num_rounds: an integer noting how many rounds that the game will go on for.
        :param num_code_slots: an integer dictating how many slots there are to fill in the Mastermind game.
        :param num_colors: an integer declaring the number of colors that will be used in the Mastermind game.
        :return: None.
        """
        self.solution.clear()
        self.memory.clear()
        solution_gen_index: int = num_code_slots
        while solution_gen_index > 0:
            self.solution.append(MMColor(random.randint(1, num_colors)))
            solution_gen_index -= 1
        self.game_introduction()
        self.play_mastermind(num_rounds, num_code_slots, num_colors)

    @staticmethod
    def game_introduction() -> None:
        """
        This method plays the introduction to the game and reminds the user of its commands.
        :return: None.
        """
        print("Welcome to Mastermind.")
        print("The solution for this round has been generated. Let's begin, shall we?")
        input("Press enter to continue.")
        print("")
        print("Enter answers as a sequence of four letters representing colors in the code.")
        print("To remind yourself of what colors are available for use, type 'colors' here.")
        print("To remind yourself of your past entries and results, type 'memory' here.")

    def play_mastermind(self, num_rounds: int, num_code_slots: int, num_colors: int) -> None:
        """
        This method sets the Mastermind game in motion.
        :param num_rounds: an integer noting how many rounds that the game will go on for.
        :param num_code_slots: an integer dictating how many slots there are to fill in the Mastermind game.
        :param num_colors: an integer declaring the number of colors that will be used in the Mastermind game.
        :return: None.
        """
        while num_rounds > 0:
            if num_rounds == 1:
                print("You have " + str(num_rounds) + " round left.")
            else:
                print("You have " + str(num_rounds) + " rounds left.")

            mm_input: str = input(">> ")
            if mm_input == "colors":
                self.print_colors(num_colors)
            elif mm_input == "memory":
                self.print_memory()
            else:
                mm_input: list = self.convert_input(mm_input, num_code_slots, num_colors)
                if self.is_valid_input(mm_input, num_code_slots):
                    analysis: list = self.analyze_combination(mm_input)
                    if analysis[0] == num_code_slots:
                        self.victory_screen()
                        break
                    else:
                        self.memory.append([mm_input, analysis])
                        print("That result was not correct.")
                        print("Your input was: " + str(mm_input) + ".")
                        print("The result was: " + str(analysis[0]) + " colors are correct and " +
                              str(analysis[1]) + " are in the wrong place.")
                        num_rounds -= 1
                else:
                    print("That input was invalid. Please try again.")
        else:
            print("Sorry, you're out of time. This game is over.")
            print("The winning combination was: " + str(self.solution) + ".")
            print("Redirecting you back to the main menu...")
            time.sleep(3)
            print("You are back on the main menu.")

    @staticmethod
    def print_colors(num_colors: int) -> None:
        """

        :param num_colors: an integer declaring the number of colors that are used in the Mastermind game.
        :return:
        """
        color_index: int = 1
        while color_index <= num_colors:
            print(MMColor(color_index))
            color_index += 1

    def print_memory(self) -> None:
        """

        :return:
        """
        if len(self.memory) == 0:
            print("There are no former entries to print.")
        else:
            print("Entry Format: Number of Entry. [Input Sequence]; [Number Correct, Number in Wrong Place]")
            for index, prior_input in enumerate(self.memory):
                print(str(index + 1) + ". " + str(prior_input[0]) + "; " + str(prior_input[1]))

    @staticmethod
    def convert_input(mm_input: str, num_code_slots: int, num_colors: int) -> list:
        """
        This method converts the player's given input into a usable form for processing.
        :param mm_input: a list containing the user's input for guessing the Mastermind game's solution.
        :param num_code_slots: an integer dictating how many slots there are to fill in the Mastermind game.
        :param num_colors: an integer declaring the number of colors that are used in the Mastermind game.
        :return:
        """
        mm_input = mm_input.strip().upper().replace(' ', '')
        input_result: list = []
        if len(mm_input) <= num_code_slots:
            for char in mm_input:
                try:
                    if MMColor[char] and MMColor[char].value <= num_colors:
                        input_result.append(MMColor[char])
                except KeyError:
                    pass
        return input_result

    @staticmethod
    def is_valid_input(mm_input: list, num_code_slots: int) -> bool:
        """
        This method determines whether the user's given input is of a valid form for the Mastermind game.
        In other words, there must be only valid color abbreviations and there must be a number of them
        equivalent to the number of code slots.
        :param mm_input: a list containing the user's input for guessing the Mastermind game's solution.
        :param num_code_slots: an integer dictating how many slots there are to fill in the Mastermind game.
        :return: a bool as to whether the given input is valid.
        """
        validity: bool = True
        if mm_input and (num_code_slots == len(mm_input)):
            for item in mm_input:
                if not isinstance(item, MMColor):
                    validity = False
        else:
            validity = False
        return validity

    def analyze_combination(self, current_guess: list) -> list:
        """
        This method determines how many items in an attempted solution are in the right place
        and how many are in the wrong place.
        :param current_guess: a list of MMColors representing the player's present guess.
        :return: a list of two integers. The first indicates the number of colors that the player
        had in the correct location; the second indicates the number of colors that the player
        had in the incorrect location.
        """
        num_correct: int = 0
        num_wrong_place: int = 0
        temp_solution: list = copy.deepcopy(self.solution)
        wrong_place_candidates = []
        for index, color in enumerate(current_guess):
            if color == self.solution[index]:
                num_correct += 1
                temp_solution[index] = True
            elif color in temp_solution:
                wrong_place_candidates.append(color)

        for index, color in enumerate(wrong_place_candidates):
            if color in temp_solution:
                for i, item in enumerate(temp_solution):
                    if color == item:
                        temp_solution[i] = True
                        break
                num_wrong_place += 1
        return [num_correct, num_wrong_place]

    @staticmethod
    def victory_screen() -> None:
        """
        This method displays text upon winning Mastermind.
        :return: None.
        """
        print("Congratulations! That was the correct combination! You won!")
        print("Returning to the main menu...")
        time.sleep(5)
        print("You are back on the main menu.")


new_game: Mastermind = Mastermind()
