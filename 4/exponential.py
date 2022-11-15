import math


# Calculating the exponential function.
def expo_slow(x, acc = 0.00001):
  sum = 0
  i = 0
  while True:
    wyn = (x ** i) / math.factorial(i)
    sum += wyn
    if( wyn < acc ):
      return sum
    i += 1

def expo(x, epsilon=0.001):
    suma = 1
    an = 1
    n = 1
    while True:
        an *= x/n
        suma += an
        if abs(an) < epsilon:
            return suma
        n += 1


print(expo(1))
print(expo_slow(1))
