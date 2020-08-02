# funkcja sprawdzajaca wystapienia danej liczby w liście


from collections import Counter
lista = [1,  2, 2, 3, 4, 4, 5, 5, 5]

#sposób 1

def policz_wystapienia(lista):
    return dict(Counter(lista))
print(policz_wystapienia(lista))

#sposób 2

def policz_wystapienia(lista):
    moj_slownik = {}
    for x in lista:
        if x not in moj_slownik:
            moj_slownik[x] = 1
        elif x in moj_slownik:
            moj_slownik[x] += 1
    return moj_slownik
print(policz_wystapienia(lista))
