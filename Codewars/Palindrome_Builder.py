# Task
# Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.
#
# Example
# For the input cdcab, the output should be bacdcab

#  abac - cabac kajak

def build_palindrome(word):
    if len(word) > 10 and len(word) < 3:
        pass

    for i in range(len(word)):
        if word[i] != word[len(word)-1 - i]:
            word = word[::-1] + word[len(word)-1 - i]
    return word[::-1]




print(build_palindrome('bacb'))



