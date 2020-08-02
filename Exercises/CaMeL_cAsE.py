# Biedny Camel Case
# Zaimplementuj funkcję, która dla wprowadzonego przez użytkownika ciągu znaków zwróci mu biednego CamelCase’a zgodnie z przykładem w tekście.
# Załóż, że program nie będzie wczytywał polskich znaków, a spacja nie jest liczona jako litera (jest przepisywana).
# # Jak się cieszę -> JaK sIę CiEsZę

#
text = input("Podaj tekst ")
def camelcase(str):
    list = [] # tworzymy pusta liste w której bedziemy przechowywać zmieniony tekst
    index = 0 # tworzymy licznik który bedzie decydowal czy litera ma zostać zmieniona na dużą czy nie. licznik bedzie się zwiekszał o 1 dla litery i o 2 dla spacji lub przecinka.
    for i in text:
        if i == " " or i == ",":
            list.append(i)
            index += 2 # jezeli pod indeksem nie znajduje sie litera tylko spacja lub przecinek to przepisujemy spację lub przecinek a indeks zwiększamy o 2.
        elif index % 2 == 0: # jeżeli indeks jest liczbą parzystą to znajdującą się pod nim literę zamieniamy na dużą.
            list.append(i.upper())
            index += 1
        else: #jeżeli indeks jest liczbą nieparzystą to znajdującą się pod nim literę niezamieniamy.
            list.append(i.lower())
            index += 1
    return ''.join(list)                                        #Join/ pamietaj zmienia liste na tekst i tu zwraca
print(camelcase(text)) # wywołujemy funkcję podając konkretny tekst do "skamelowania"



