import sys


sys.set_int_max_str_digits(99999999)

def potega(x, n):
  if(n == 1): return x
  elif(n == 0): return 1 
  
  potega_polowy = potega(x, n // 2)
  if(n % 2 == 0):
    return potega_polowy * potega_polowy
  else:
    return potega_polowy * potega_polowy * x
  
def altPotega(x, n):
  # this function works by using the binary representation of n
  w = 1
  while n != 0:
    if n%2 == 1:
      w *= x
    x *= x
    n //= 2
  return w

  
print(altPotega(2, 5))