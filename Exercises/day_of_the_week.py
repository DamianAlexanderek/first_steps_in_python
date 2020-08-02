# Zaimplementuj funkcje wyznaczającą dzien tygodnia za n dni.

def data(i, n):
    tupla = ("Pn", "Wt", "Sr", "Czw", "Pt", "Sb", "Nd") # tworzymy krotke ze skrótami wszystkich dni tygodnia
    return tupla[tupla.index(i) + n %7]
print(data("Wt", 9))