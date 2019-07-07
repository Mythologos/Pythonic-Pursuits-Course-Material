# Lecture One: Exercise Three
def create_madlib(noun, verb, adjective, adverb):
    # type: (str, str, str, str) -> None
    madlib_noun(noun)
    madlib_verb(noun, verb)
    madlib_adjective(noun, adjective)
    madlib_adverb(noun, adverb)


def madlib_noun(noun):
    print("There once was a " + noun + " deep in the sea.")


def madlib_verb(noun, verb):
    print("Here and there, the " + noun + " " + verb + " freely.")


def madlib_adjective(noun, adjective):
    print("As a result, the " + noun + " became " + adjective + ".")


def madlib_adverb(noun, adverb):
    print("And, thus, the " + noun + " lived " + adverb + " ever after.")


create_madlib("mouse", "gurgled", "dead", "emptily")
print("")
create_madlib("warhead", "exploded", "boiling hot", "foggily")
print("")
create_madlib("ear", "ate", "eloquent", "eerily")
