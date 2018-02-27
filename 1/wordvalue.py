from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY, "r") as words:
        return words.read().split()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word.upper():
        if letter in LETTER_SCORES.keys():
            value += LETTER_SCORES[letter]
    return value

def calc_word_valueAlt(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter, 0) for letter in word.upper())

def max_word_value(words = ''):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    highestValueWord  = words[0]
    highestValue = calc_word_value(highestValueWord)

    for word in words:
        if calc_word_value(word) > highestValue:
            highestValueWord = word
            highestValue = calc_word_value(word)
    return highestValueWord

def max_word_valueAlt(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words or load_words(), key = lambda word: calc_word_valueAlt(word))

if __name__ == "__main__":
    # execute only if run as a script
    print(max_word_value())

    pass