import math

# oblicz pole funkcji
def pole_funkcji(f, start, koniec, n = 100):
  # co ile ma być liczone pole
  diff = (koniec-start)/n
  
  pole = 0
  ost_h = f(start)
  
  x = start
  for _ in range(1, n):
    x += diff
    akt_h = f(x)
    pole += ((ost_h + akt_h) * diff)
    ost_h = akt_h
  
  akt_h = f(koniec)
  pole += ((ost_h + akt_h) * diff)
  
  return pole / 2

# oblicz pole funkcji
def moje_opt_pole_funkcji(f, start, koniec, n = 100):
  # co ile ma być liczone pole
  diff = (koniec-start)/n
  
  pole = 0
  ost_h = f(start)
  
  x = start
  for _ in range(1, n):
    x += diff
    akt_h = f(x)
    pole += ((ost_h + akt_h))
    ost_h = akt_h
  
  akt_h = f(koniec)
  pole += ((ost_h + akt_h))
  
  return (pole * diff) / 2

def pole_funkcji_z_tablicy(start,koniec,n,f):
  diff = (koniec-start)/n
  
  x = start + diff
  
  s = (f(start) + f(koniec))/2
  
  # the above line is necessary since the first and last elements only occur once
  # and the for loop below only adds the elements that occur twice (the ones in the middle),
  # because x is already incremented by diff in the first iteration, and range(n-1) assures that
  # the last element is not included
  
  # (a+b)/2 + (b+c)/2 + (c+d)/2 = b+c + (a/2 + d/2) = b+c + (f(start) + f(koniec))/2
  for _ in range(n-1):
    s += f(x)
    x += diff
    
  s *= diff
  return s
  
def sinP1(x):
  return math.sin(x)

# print(pole_funkcji(sinP1, 0, math.pi, 50000000))
print(pole_funkcji_z_tablicy(0, 2, 4, lambda x: 1))
print(moje_opt_pole_funkcji(lambda x: 1, 0, 2, 4))