# napisz program który ustawi wszytskie 1 z listy po jej prawej stronie.

lista = [1,2,1,6,8,1,2 ,1,3,25,88,1,9,2]

# sposób 1

def jedynka_na_prawo(lista):
    for _ in range(lista.count(1)):
        lista.append(lista.pop(lista.index(1)))
jedynka_na_prawo(lista)
print(lista)

#sposób 2

def jedynka_na_prawo(lista):
    for _ in range(lista.count(1)):
        lista.remove(1)
        lista.append(1)
jedynka_na_prawo(lista)
print(lista)

