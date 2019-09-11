# Bridge One: Exercise Three
def remove_punctuation(string):
    # The '\'s here tell Python that the text continues onto the next line.
    # It is useful for keeping all the text on one screen.
    return string.replace(".", "").replace(",", "").replace("!", "") \
        .replace("?", "").replace(":", "").replace(";", "").replace("'", "") \
        .replace('"', '')


print(remove_punctuation("Here's the gist of it: your shock when you saw the body tells me " +
                         "everything I needed to know. Aren't I right? You definitely saw the corpse beforehand; " +
                         "the only reason you'd have to hide that fact ... is that you are the murderer yourself!"))
