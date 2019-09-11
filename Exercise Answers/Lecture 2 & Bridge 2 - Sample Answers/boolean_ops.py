def NOT(bool1):
    return_value = True
    if bool1:
        return_value = False
    return return_value


def AND(bool1, bool2):
    return_value = False
    if bool1:
        if bool2:
            return_value = True
    return return_value


def OR(bool1, bool2):
    return_value = False
    if bool1:
        return_value = True
    elif bool2:
        return_value = True
    return return_value


# not operator:
print(NOT(True)) # should return False
print(NOT(False)) # should return True

# and operator:
print(AND(True, True)) # should return True
print(AND(True, False)) # should return False
print(AND(False, True)) # should return False
print(AND(False, False)) # should return False

# or operator:
print(OR(True, True)) # should return True
print(OR(True, False)) # should return True
print(OR(False, True)) # should return True
print(OR(False, False)) # should return False
