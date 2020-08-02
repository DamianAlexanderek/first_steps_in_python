# NWD w sposób iteracyjny

def nwd(a,b): #dla liczby 2 i 8: nwd (2,8) więc jest nic innego jak 2x8/8
    while a != b:
        if a > b:
            a -= b #7-6=1
        else:
            b -= a #8-2=6
    return a
print(nwd(2,8))

# NWD w sposób rekurencyjny

def nwd(a,b):
    if b != 0:
        return nwd(b, a%b) #nwd(18, 12/18= %6,
    else:
        return a

print(nwd(12,18))