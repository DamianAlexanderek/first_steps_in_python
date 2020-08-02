# wyliczane sumy cyfr w liczbie -- >  rekurencyjnie

def suma(n:int):
    if n > 0:
        return n%10 + suma(n//10)  # n // 10
    return 0

print(suma(1234))




