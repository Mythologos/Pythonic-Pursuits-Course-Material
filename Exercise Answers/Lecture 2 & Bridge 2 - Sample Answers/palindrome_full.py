def reverse(sequence):
    """
    The following function takes a string. It returns that string in a reversed order.
    :param sequence: a string to be reversed.
    :return: a string having been reversed.
    """
    return sequence[::-1]


def is_palindrome(string):
    palindrome_bool = False
    if string == reverse(string):
        palindrome_bool = True
    return palindrome_bool


print(is_palindrome("turnaround"))  # should return False
print(is_palindrome("racecar"))  # should return True
