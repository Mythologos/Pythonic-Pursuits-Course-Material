# Lecture 2, Exercise 2:

# This is fine, but I'd expect them to do it via nested loops rather than a global variable.
main_menu_value: int = 1

def startMenu():
    loop_condition: bool = True
    while(loop_condition):
        menuDialogue(main_menu_value)
        user_input: str = input(">> ").strip()
        if(user_input == "Start"):
            startDialogue()
            input("Press enter to continue. (1/1)")
        elif(user_input == "Help"):
            helpDialogue()
            input("Press enter to continue. (1/1)")
        elif(user_input == "Options"):
            optionsMenu()
        elif(user_input == "Quit"):
            loop_condition = False
        else:
            print("That input is not recognized. Please try again.")
        print("")

def menuDialogue(mm_value):
    if(mm_value == 1):
        print('--- MAIN MENU ---')
        print('     - Start')
        print('     - Help')
        print('     - Options')
        print('     - Quit')
    elif(mm_value == 2):
        print('~~~~~ M A I N  M E N U ~~~~~')
        print('     ~ Start')
        print('     ~ Help')
        print('     ~ Options')
        print('     ~ Quit')
    elif(mm_value == 3):
        print('* M * A * I * N * * M * E * N * U *')
        print('     * Start')
        print('     * Help')
        print('     * Options')
        print('     * Quit')
    elif(mm_value == 4):
        print('/ MAIN MENU \\')
        print('     | Start')
        print('     | Help')
        print('     | Options')
        print('     | Quit')

def startDialogue():
    print("This game isn't available yet. Sorry!")

def helpDialogue():
    print("On the start menu, current commands are: Start, Help, Options, and Quit.")
    print("If this was a game program, Start would run the game.")
    print("Meanwhile, Help gives this dialogue.")
    print("The Options menu allows for changes to the menu to be made.")
    print("Lastly, Quit ends the program.")

def optionsMenu():
    loop_condition: bool = True
    while(loop_condition):
        optionsDialogue()
        user_input: str = input(">> ").split()
        if(user_input == "Help"):
            optionsHelpDialogue()
            input("Press enter to continue. (1/1)")
        elif(user_input == "Controls"):
            print("This is where options for controls would go!")
            input("Press enter to continue. (1/1)")
        elif(user_input == "Game"):
            print("This is where the game options would go!")
            input("Press enter to continue. (1/1)")
        elif(user_input == "Menu"):
            print("There are four menus to select from! They are: ")
            print('     1. Dashes')
            print('     2. Tildes')
            print('     3. Stars')
            print('     4. Slashes')
            print("Please select an option by number.")
            switchMenu(input(">> ").split())
            input("Press enter to continue. (1/1)")
        elif(user_input == "Back"):
            print("Proceeding back to the main menu...")
            loop_condition = False
        else:
            print("That input is not recognized. Please try again.")
            input("Press enter to continue. (1/1)")

def optionsDialogue():
    print('--- OPTIONS ---')
    print('     - Help')
    print('     - Controls')
    print('     - Game')
    print('     - Menu')
    print('     - Back')

def optionsHelpDialogue():
    print("On the options menu, current commands are: Help, Controls, Game, Menu, and Back.")
    print("Help brings up this menu.")
    print("Controls displays a message and would allow for a change of controls.")
    print("Game displays a message and would allow for change in options for the game itself.")
    print("Menu allows for a change in the Main Menu. There are up to four menu options (1, 2, 3, and 4).")
    print("Back returns to the Main Menu.")

def switchMenu(menuValue):
    menuValue = int(menuValue, 10)
    if(menuValue > 0):
        if(menuValue < 5):
            global main_menu_value
            main_menu_value = menuValue
            print("The main menu has been changed.")
        else:
            print("The given value was too high. Please try again.")
    else:
        print("The given value was too low. Please try again.")


startMenu()
