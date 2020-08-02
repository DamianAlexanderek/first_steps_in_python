# Funkcja wczytuje dwie liczby. Rozpoznaje która jest większa i wypisuje w kolejności: większa, mniejsza. Jeżeli
# # # są równe wyświetla komunikat "Liczby są równe"

def which_one_is_bigger(a, b):
    if a == b:
        return ("Liczby są równe")
    elif a > b:
        return (f"Większa liczba to {a} a mniejsza to {b}")
    else:
        return (f"Większa liczba to {b} a mniejsza to {a}")


print(which_one_is_bigger(8, 6))
