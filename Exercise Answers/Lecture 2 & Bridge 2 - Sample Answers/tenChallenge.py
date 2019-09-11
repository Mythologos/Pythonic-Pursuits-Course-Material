# Lecture 2, Exercise 3:
def when_ten_v2(number):
    if number == 10:
        print("Done!")
    elif number > 10:
        print("Too high!")
        when_ten_v2(number - 1)
    else:
        print("Too low!")
        when_ten_v2(number + 1)


def when_ten_v3(number):
    difference: int = number - 10
    if difference == 0:
        print("Done!")
    elif difference > 0:
        print("Too high!")
        number = number - difference
    elif difference < 0:
        print("Too low!")
        number = number - difference
    print(number)
    print(difference)


print("when_ten_v2:")
when_ten_v2(10)
when_ten_v2(15)
when_ten_v2(5)
print("")
print("when_ten_v3:")
when_ten_v3(10)
when_ten_v3(15)
when_ten_v3(5)
