# silnia obliczana iteracyjnie

def silnia(n:int):
    result = 1
    for i in range(1, n+1):
        result = result *i
    return result
print(silnia(5))
#
# # 0! = 1, 1! = 1, n! = n*(n-1)!


# silnia obliczna rekurencyjnie

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)  # 3x (3-1), 2x(2-1), 1x2, 2x3, 3x4 ...

print ( factorial(5) )