# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"

def is_anagram(test, original):
    tab = []
    tab1 = []

    for i in test:
        if i.isalpha():
            tab += [i.lower()]

    for i in original:
        if i.isalpha():
            tab1 += [i.lower()]

    tab.sort(key=str)
    tab1.sort(key=str)

    if tab == tab1:
        return True
    else:
        return False
    pass