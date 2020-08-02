'''
Zaimplementuj funkcję person_descriptior która:
- po podaniu liczby mniejszej niż 0 wywoływany jest ValueError
- po podaniu liczby mniejszej od 18 zwracany jest tekst : "Nastolatek"
- po podaniu liczby mniejszej od 30 zwracany jest tekst : "Młody"
- po podaniu liczby mniejszej od 50 zwracany jest tekst : "Dojrzały"
- po podaniu liczby mniejszej od 70 zwracany jest tekst : "Wiekowy"
- po podaniu liczby większej lub równej od 70 zwracany jest tekst : "Na emeryturze"
Napisz testy jednostkowe do zaimplementowanej funkcji
'''



def person_descriptior(i = int):
    if i < 0:
        raise ValueError()
    elif i >= 0 and i <= 18:
        return "Nastolatek"
    elif i > 18 and i <= 30:
        return "Młody"
    elif i > 30 and i <= 50:
        return "Dojrzały"
    elif i > 50 and i < 70:
        return "Wiekowy"
    else:
        return "Na emeryturze"
# while 1:
#     i = input("Podaj liczbę: ")
#     person_descriptior(int(i))

