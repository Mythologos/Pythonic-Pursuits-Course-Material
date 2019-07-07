# Lecture One: Exercise Two
def quoting(name, quote):
    print("As " + name + " said once before, " + quote)


# Not my favorite quotes, but they work.
def favorite_quotes():
    quoting("someone unknown",
            '"Yesterday is history, tomorrow is a mystery, but today is a gift. ' +
            'That is why they call it the present."')
    quoting("Elie Wiesel", '"The opposite of love is not hate; it\'s indifference."')
    quoting("Jonathan Swift", '"May you live all the days of your life."')


favorite_quotes()
