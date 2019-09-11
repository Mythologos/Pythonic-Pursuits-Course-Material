def count_both_ways(snippet, phrase):
    phrase = phrase + '|' + phrase[::-1]
    double_count = 0
    while snippet in phrase:
        if phrase.startswith(snippet):
            double_count = double_count + 1
        phrase = phrase.lstrip(phrase[0])
    return double_count


print(count_both_ways('ab', 'when i am able, i will go back inside.'))  # should return 2
print(count_both_ways('aw', 'if a swatch of the paint was watery,  what does that say about the product?'))  # should return 3
print(count_both_ways('b', "there's nothing to be afraid of but me."))  # should return 4
print(count_both_ways('xy', 'are you ready?'))  # should return 0
print(count_both_ways('ti', 'this is it!'))  # should return 1
