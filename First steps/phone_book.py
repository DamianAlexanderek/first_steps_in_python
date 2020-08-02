# Mój pierwszy program EVER. Mnóstwo radosci i zabawy przy pisaniu tego programu.

# Stwórz książkę telefoniczną za pomocą kolekcji słownikowej.
# Kluczem będzie imię użytkownika a wartością numer telefonu.
# Program powinien mieć menu główne i działać w pętli nieskończonej,
# póki użytkownik nie wpisze litery q.
# - Program powinien spełniać takie funkcjonalności jak dodawanie
# nowego wpisu do książki z klawiatury komputera.
# - Usuwanie wpisu z książki telefonicznej za pomocą danego imienia.
# - Wyszukiwanie po imieniu numeru telefonu.

ksiazka_telefoniczna = {}
nazwa = ""
numer = 0
liczba_kontaktow = 0
while 1:
    print("*"*46)
    print("*"*12, "Książka telefoniczna","*"*12)
    print("*" * 46)
    print("Menu:")
    print("Wpisz 'a' aby dodać nowy kontakt")
    print("Wpisz 'b' aby usunąć kontakt")
    print("Wpisz 'c' aby wyszukać kontakt")
    print("Wpisz 'd' aby wyświetlić wszystkie kontakty")
    print("Wpisz 'q' jeśli chcesz zakończyć program")
    komenda = input()
    if komenda == "q" or komenda == "Q":
        print("Program zakończony")
        break
    elif komenda == "a" or komenda == "A":
        nazwa = input("Wpisz nazwę nowego kontaktu: ")
        if nazwa in ksiazka_telefoniczna:
            print(f"W książce telefonicznej znajduję się już kontakt o nazwie: {nazwa}")
            rename = input("Czy chcesz go zastąpić? Wpisz: TAK lub NIE:  ")
            if rename == "tak" or rename == "Tak" or rename == "TAK":
                ksiazka_telefoniczna.pop(nazwa)
                numer = int(input("Wpisz numer nowego kontaktu: "))
                print(f"Czy na pewno chcesz zapisać nowy kontakt '{nazwa} {numer}'")
                upewnienie = input("Wpisz: TAK lub NIE: ")
                ksiazka_telefoniczna[nazwa] = numer
                print("Kontakt został zaktualizowany.!")
            elif rename == "nie" or rename == "Nie " or rename == "NIE":
                print("Powrót do menu głównego")
            else:
                print(f"W ksiązce telefonicznej znajduję się już kontakt o nazwie: {nazwa}")
                rename = input("Czy chcesz go zastąpić? Wpisz: TAK lub NIE:  ")
        else:
            numer = input("Wpisz numer nowego kontaktu: ")
            if numer.isdigit():
                print(f"Czy na pewno chcesz zapisać nowy kontakt '{nazwa} {numer}'")
                upewnienie = input("Wpisz: TAK lub NIE: ")
                if upewnienie == "TAK" or upewnienie == 'tak' or upewnienie == "Tak":
                    ksiazka_telefoniczna[nazwa] = numer
                    print("Nowy kontakt został dodany do twojej książki telefonicznej!")
                    liczba_kontaktow += 1
                else:
                    print("Kontakt nie został dodany do twojej książki telefonicznej!")
            else:
                print("Numer telefonnu powinine składać się wyłącznie z liczb!")
    elif komenda == "b" or komenda == "B":
        nazwa = input("Wpisz nazwę kontaktu który chcesz usunąć: ")
        if nazwa in ksiazka_telefoniczna:
            print(f"Czy na pewno chcesz usunąć kontakt '{nazwa} {ksiazka_telefoniczna.get(nazwa)} '")
            upewnienie = input("Wpisz: TAK lub NIE: ")
            if upewnienie == "TAK" or upewnienie == 'tak' or upewnienie == "Tak":
                ksiazka_telefoniczna.pop(nazwa)
                print("Kontakt został usunięty z twojej książki telefonicznej!")
                liczba_kontaktow -= 1
            else:
                print("Kontakt nie został usunięty z twojej książki telefonicznej!")
        else:
            print(f"Kontakt {nazwa} nie istnieje.")
    elif komenda == "c" or komenda == "C":
        nazwa_szukaj = input("Wpisz nazwe kontaktu którego szukasz: ")
        if nazwa_szukaj in ksiazka_telefoniczna:
            print(f"Wynik wyszukiwania: {nazwa_szukaj} numer: {ksiazka_telefoniczna.get(nazwa_szukaj)}")
        elif nazwa_szukaj not in ksiazka_telefoniczna:
            print(f"Kontakt o nazwie {nazwa_szukaj} nie istnieje. Chcesz dodać go do ksiązki telefonicznej?")
            upewnienie = input("Wpisz: TAK lub NIE: ")
            if upewnienie == "TAK" or upewnienie == 'tak' or upewnienie == "Tak":
                numer = input(f"Wpisz numer nowego kontaktu {nazwa_szukaj}: ")
                if numer.isdigit():
                    print(f"Czy na pewno chcesz zapisać nowy kontakt '{nazwa_szukaj} {numer}'")
                    upewnienie = input("Wpisz: TAK lub NIE: ")
                    if upewnienie == "TAK" or upewnienie == 'tak' or upewnienie == "Tak":
                        ksiazka_telefoniczna[nazwa_szukaj] = numer
                        print("Nowy kontakt został dodany do twojej książki telefonicznej!")
                        liczba_kontaktow += 1
                    else:
                        print("Kontakt nie został dodany do twojej książki telefonicznej!")
                else:
                    print("Numer telefonnu powinine składać się wyłącznie z liczb!")
        else:
            print(f"Kontak o nazwie {nazwa_szukaj} nie isnieje!")
    elif komenda == "d" or komenda == "D":
        print(f"Wszystkie kontakty: {liczba_kontaktow}")
        print(ksiazka_telefoniczna)
    else:
        print("Podana funkcja nie istnieje. Spróbuj ponownie.")