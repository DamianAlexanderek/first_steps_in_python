# Zaimplementuj poniższą funkcję:
# W celu zaoszczędzenia ilości znaków w krótkich wiadomościach tekstowych (SMS) nie pisze się spacji,a każdy wyraz rozpoczyna się wielką literą.
# Twoim zadaniem jest otrzymany tekst przerobic zgodnie z powyższym trendem.
# Tekst wprowadzony z wejścia, ale bez spacji. Ponadto każdy wyraz poprzedzony na wejściu spacją zaczyna się wielką literą.
# Ma to wygladac tak: Input: "Dzisiaj jest czwartek A jutro bedzie piatek."
#                     Output: "DzisiajJestCzwartekAJutroBedziePiatek."

import string # importujemy moduł string

text = input("Podaj tekst ")
a = string.capwords(text) # do zmiennej a przypisujemy zmieniony tekst, w którym dzieki funkcji capwords, wszystkie pierwsze litery w zdaniu zamieniane są na duże.
print(a.replace(" ", "")) # funkcja replace zamienia spację na pusty string(brak odstepu)
