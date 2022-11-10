import math

# oblicz pole funkcji
def pole_funkcji(f, start, koniec, n = 100):
  # co ile ma być liczone pole
  diff = (koniec-start)/n
  
  pole = 0
  ost_h = f(start)
  
  x = start
  for _ in range(1, n + 1):
    x += diff
    akt_h = f(x)
    pole += ((ost_h + akt_h) * diff) / 2
    ost_h = akt_h
  
  return pole
  
def sinP1(x):
  return 1

print(pole_funkcji(sinP1, 0, 10, 100))