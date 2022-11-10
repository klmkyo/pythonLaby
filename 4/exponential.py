import math


def expo(acc = 0.001):
  sum = 0
  i = 0
  while True:
    wyn = (1 ** i) / math.factorial(i)
    sum += wyn
    if( wyn < acc ):
      return sum
    i += 1

print(expo(0.000001))