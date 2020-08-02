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

def is_palindrom(word):
    return word == word[::-1] # bardzo przydatny [::-1] zapis który zwraca nam wyraz czytany/pisany od tyłu
print(is_palindrom("kajak"))
print(is_palindrom("kajjak"))
print(is_palindrom("kajjakk"))
