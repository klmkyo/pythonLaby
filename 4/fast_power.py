import sys


sys.set_int_max_str_digits(99999999)

def potega(x, n):
  if(n == 1): return x
  elif(n == 0): return 1 
  
  wynik_polowy = potega(x, n // 2)
  if(n % 2 == 0):
    return wynik_polowy * wynik_polowy
  else:
    return wynik_polowy * wynik_polowy * x
  
def altPotega(x, n):
  w = 1
  while n != 0:
    if n%2 == 1:
      w *= x
    x = x*x
    n //= 2
  return w

  
print(altPotega(43, 90))