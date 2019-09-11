def factorial(number):
    result: int = 1
    while number >= 1:
        result = result * number
        number = number - 1
    return result


print(factorial(0))  # should return 1
print(factorial(1))  # should return 1
print(factorial(3))  # should return 6
print(factorial(4))  # should return 24
print(factorial(5))  # should return 120
