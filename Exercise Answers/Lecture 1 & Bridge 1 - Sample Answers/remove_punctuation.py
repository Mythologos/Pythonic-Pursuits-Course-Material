# Bridge One: Exercise Three
def remove_punctuation(string):
    # The '\'s here tell Python that the text continues onto the next line.
    # It is useful for keeping all the text on one screen.
    return string.replace(".", "").replace(",", "").replace("!", "") \
        .replace("?", "").replace(":", "").replace(";", "").replace("'", "") \
        .replace('"', '')


print(remove_punctuation("""Here's the gist of it: "What are those?!" is a dumb meme. Don't talk to me again; I don't want to hear your low-brow humor any more, cretin."""))
