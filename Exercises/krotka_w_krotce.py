# czy krotka1 zawiera się w krotce2
krotka1 = (3, 4, 5)
krotka2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# def czy_krotka_w_krotce(krotka1, krotka2):
#     licznik = 0
#     for element in krotka1:
#         if element in krotka2:
#             licznik +=1
#     if licznik == len(krotka1):
#         return True
#     else:
#         return False
# print(czy_krotka_w_krotce(krotka1, krotka2))

# def czy_krotka_w_krotce(krotka1, krotka2):
#     for element in krotka1:
#         if element not in krotka2:
#             return False
#     return True
# print(czy_krotka_w_krotce(krotka1, krotka2))

from collections import Counter

def check_tuples(tup1: tuple, tup2: tuple) -> bool:
    counter1 = Counter(tup1)
    counter2 = Counter(tup2)
    return counter1 == counter2

if __name__ == '__main__':
    tup1 = (1, 2, 2, 3, 4, 4, 4)
    tup2 = (4, 4, 4, 1, 2, 2, 3)
    tup3 = (4, 4, 4, 1, 2, 2, 2)
    tup4 = (4, 4, 4, 1, 2, 2, 3, 4)
    print(check_tuples(tup1, tup2))
    print(check_tuples(tup1, tup3))
    print(check_tuples(tup1, tup4))
    print(check_tuples(tup2, tup3))
    print(check_tuples(tup2, tup4))
    print(check_tuples(tup2, tup1))
