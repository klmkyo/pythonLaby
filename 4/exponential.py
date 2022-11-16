import math


# Calculating the exponential function.
def expo_slow(x, acc=0.00001):
    sum = 0
    n = 0
    while True:
        wyn = (x ** n) / math.factorial(n)
        sum += wyn
        if (wyn < acc):
            return sum
        n += 1


def expo(x, epsilon=0.00001):
    suma = 1
    an = 1
    n = 1
    while abs(an) > epsilon:
        an *= x/n
        suma += an
        n += 1
    return suma


print(expo(1))
print(expo_slow(1))
