from decimal import DivisionByZero
from math import sqrt

def getNumber(text: str):
  while True:
    try:
      x = float(input(text))
      break
    except ValueError:
      print("Podana wartość nie jest liczbą!")
  return x

def getNonZero(text: str):
  while True:
    try:
      x = getNumber(text)
      if(x==0):
        raise DivisionByZero
      break
    except DivisionByZero:
      print("Podano a równe 0")
      pass
  return x

a = getNonZero("Podaj a: ")
b = getNumber("Podaj b: ")
c = getNumber("Podaj c: ")
  
delta = b*b - 4*a*c

if(delta < 0):
  print("Brak rozwiązań rzeczywistych")
  exit(0)

sqrt_delta = sqrt(delta)

if(a == 0):
  print("Podana funkcja nie jest kwadratowa! (a = 0)")
  exit(1)

x1 = (-b + sqrt_delta) / (2*a)
x2 = (-b - sqrt_delta) / (2*a)

print()

if(delta == 0):
  print(f"x = {x1}")
else:
  print(f"x1 = {x1}")
  print(f"x2 = {x2}")