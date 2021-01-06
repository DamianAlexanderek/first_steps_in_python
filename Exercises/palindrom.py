# zaimplementuj funkcje w której sprawdzisz czy podany wyraz jest palindromem

#sposób 1

# def is_palindrom(word):
#     palindrom = True
#     for x in range(len(word)):
#         if word[x] != word[len(word) - 1-x]:
#             return  False
#     return palindrom
# print(is_palindrom("kajak"))
# print(is_palindrom("kajjak"))
# print(is_palindrom("kajjakk"))

#sposób 2

# def is_palindrom(word):
#     return word == word[::-1] # bardzo przydatny [::-1] zapis który zwraca nam wyraz czytany/pisany od tyłu
# print(is_palindrom("kajak"))
# print(is_palindrom("kajjak"))
# print(is_palindrom("kajjakk"))

# sposób 3

import webbrowser

word = input("Input word: ")
print(word[::-1])

wordalpha = "".join([char for char in word if char.isalpha()]).lower()
invalpha = wordalpha[::-1]

print("Sequence: "" + word + """, end = "")
if wordalpha == invalpha:
    print(" is palindrome")
else:
    print(" isn't palindrome")

webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/" + word)

# sposób 4
#
# import webbrowser
#
# slowo = input("Podaj wyraz, lub zdanie które chcesz sprawdzic czy jest palindromem: ")
# slowo = slowo.replace(" ", "")
# print(slowo[::-1].lower())
#
# if slowo.lower() == slowo[::-1].lower():
#   print("Slowo jest palindromem")
# else:
#   print("Slowo nie jest palindromem")
#
# webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/" + slowo)