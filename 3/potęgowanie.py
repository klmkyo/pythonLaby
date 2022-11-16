
import math


def potega(x, n):
  if(n == 1): return x
  elif(n == 0): return 1
  
  wynik_polowy = potega(x, n // 2)
  if(n % 2 == 0):
    return wynik_polowy * wynik_polowy
  else:
    return wynik_polowy * wynik_polowy * x
  

print(potega(2, 8))