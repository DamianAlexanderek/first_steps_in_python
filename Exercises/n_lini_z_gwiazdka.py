# Wypisanie n lini z gwiazdką w sposób iteracyjny

def print_stars(n) ->str:
    for i in range(1, n+1):
        print(" "*(n-i)+"*"*(i*2-1))

print_stars(5)         # wywołanie funkcji

# Wypisanie n lini z gwiazdką w sposób rekurencyjny

def print_stars(x, n):
    if n > 0:
        print_stars(x+1, n-1)
    print(' ' * x, '*'* (2*n-1))
print_stars(0,5)
