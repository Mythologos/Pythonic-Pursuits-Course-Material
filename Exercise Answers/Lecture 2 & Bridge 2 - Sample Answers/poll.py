# Lecture 2, Exercise 1:
def poll(question, answer_one, answer_two, answer_three, answer_four, num_pollers):
    print("Current Poll:")
    print(question)
    print(answer_one)
    print(answer_two)
    print(answer_three)
    print(answer_four)
    print("")
    print("Give your response here:")

    a1_count: int = 0
    a2_count: int = 0
    a3_count: int = 0
    a4_count: int = 0

    while num_pollers > 0:
        poll_response: str = input(">> ")
        if poll_response == answer_one:
            a1_count = a1_count + 1
            num_pollers = num_pollers - 1
        elif poll_response == answer_two:
            a2_count = a2_count + 1
            num_pollers = num_pollers - 1
        elif poll_response == answer_three:
            a3_count = a3_count + 1
            num_pollers = num_pollers - 1
        elif poll_response == answer_four:
            a4_count = a4_count + 1
            num_pollers = num_pollers - 1
        else:
            print("That response was invalid.")
    print("Poll results:")
    print(answer_one + ": " + str(a1_count))
    print(answer_two + ": " + str(a2_count))
    print(answer_three + ": " + str(a3_count))
    print(answer_four + ": " + str(a4_count))


poll("How many errors did you get while writing this code?", "None", "Few", "Many", "Too Many", 5)
