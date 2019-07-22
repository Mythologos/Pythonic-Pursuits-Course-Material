# ...
def reverse(sequence):
    return sequence[::-1]

# ...
def isPalindrome(string):
    palindrome_bool = False
    if string == reverse(string):
        palindrome_bool = True
    return palindrome_bool


print(isPalindrome("turnaround"))
print(isPalindrome("racecar"))
