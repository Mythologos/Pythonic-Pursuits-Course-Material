# Lecture 2, Exercise 3:
def whenTenV2(number):
    if(number == 10):
        print("Done!")
    elif(number > 10):
        print("Too high!")
        number = whenTenV2(number - 1)
    else:
        print("Too low!")
        number = whenTenV2(number + 1)

def whenTenV3(number):
    difference: int = number - 10
    if(difference == 0):
        print("Done!")
    elif(difference > 0):
        print("Too high!")
        number = number - difference
    elif(difference < 0):
        print("Too low!")
        number = number - difference
    print(number)
    print(difference)

print("whenTenV2:")
whenTenV2(10)
whenTenV2(15)
whenTenV2(5)
print("")
print("whenTenV3:")
whenTenV3(10)
whenTenV3(15)
whenTenV3(5)
