def szereg(x, epsilon=0.000001):
    suma = 1
    an = 1
    n = 0
    while abs(an) > epsilon:
        an *= (-x * (2 * n-1)) / (2 * (n + 1))
        suma += an
        n += 1
    return suma
 
print(szereg(0.999))