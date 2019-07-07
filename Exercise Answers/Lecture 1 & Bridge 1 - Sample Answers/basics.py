# Lecture One: Exercise One
def personal_farewell(first_name):
    # type: (str) -> None
    print("Farewell, " + first_name.title().strip() + ".")
    print("Were you satisfied with your farewell?")
    satisfaction_rating: str = input(">> ")
    print("You said: " + satisfaction_rating)
    print("Your feedback has been recorded. Have a nice day!")


personal_farewell("Stephen")
