import time
import sys
# from functools import lru_cache

# zwiększ limit rekurencji oraz max. długość stringa reprezentującego liczbę całkowitą
# przydatne dla obliczania strzałki Knutha
# sys.setrecursionlimit(10**9)
# sys.set_int_max_str_digits(10**9)

# dekorator wypisujący czas wykonania funkcji oraz jej nazwę
def wypisz_info(funkcja):
    def wrapper(*args, **kwargs):
        # weź czas przed wykonaniem funkcji
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        print(f'Wywołano funkcję {funkcja.__name__} w czasie {time.time() - start}')
        return wynik
    return wrapper
  
  
def bezpieczny_input_int(msg: str):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print("To nie jest liczba całkowita. Spróbuj ponownie:")
      
def bezpieczny_input_float(msg: str):
  while True:
    try:
      return float(input(msg))
    except ValueError:
      print("To nie jest liczba rzeczywista. Spróbuj ponownie:")

      
@wypisz_info
def usun_powtarzajace_sie_elementy(lista: list):
  # policz ile razy każdy element występuje
  wystapienia = {}
  for elem in lista:
    if elem in wystapienia:
      wystapienia[elem] += 1
    else:
      wystapienia[elem] = 1
      
  # usuń wszystkie elementy, które występują więcej niż raz
  i = 0
  while i < len(lista):
    if wystapienia[lista[i]] > 1:
      del lista[i]
    else:
      i += 1
      
@wypisz_info
def usun_powtarzajace_sie_elementy_set(lista: list):
  # policz ile razy każdy element występuje
  byly = set()
  duplikaty = set()
  for elem in lista:
    if elem in byly:
      duplikaty.add(elem)
    else:
      byly.add(elem)
      
  # usuń wszystkie elementy, które występują więcej niż raz
  i = 0
  while i < len(lista):
    if lista[i] in duplikaty:
      del lista[i]
    else:
      i += 1
      
# generate a list of random integers
import random
random_list = [random.randint(0, 100) for _ in range(200000)]

list_1 = random_list.copy()
usun_powtarzajace_sie_elementy(list_1)

list_2 = random_list.copy()
usun_powtarzajace_sie_elementy_set(list_2)

exit()

# @lru_cache(maxsize=None)
def knuth(a: float, n: int, b: float):
  if b == 0:
    return 1
  if n == 1:
    return a ** b
  
  return knuth(a, n-1, knuth(a, n, b-1))


class Liczba:
    def __init__(self, naturalna: int, rzeczywista: float):
        self.naturalna = naturalna
        self.rzeczywista = rzeczywista

    @wypisz_info
    def __mul__(self, inna: 'Liczba'):
        # sprawdź czy inna jest typu Liczba
        if not isinstance(inna, Liczba):
            raise TypeError(
                f'Nie można przemnożyć {type(self)} przez {type(inna)}')
        return self.rzeczywista * inna.rzeczywista % self.naturalna

    @wypisz_info
    def __matmul__(self, inna: 'Liczba'):
        # sprawdź czy inna jest typu Liczba
        if not isinstance(inna, Liczba):
            raise TypeError(
                f'Nie można przemnożyć {type(self)} przez {type(inna)}')
        return knuth(self.rzeczywista, self.naturalna, inna.rzeczywista)
      
    def __str__(self):
      return f"Liczba({self.naturalna}, {self.rzeczywista})"


# get a list from user input
a = []
print("Podaj elementy listy (po każdym enterze):")

while True:
  inp = input()
  if inp == "":
    break
  a.append(inp)
  
usun_powtarzajace_sie_elementy(a)
print(a)

print()

def liczba_z_input(n: int) -> Liczba:
  liczba_naturalna = bezpieczny_input_int(f"Liczba {n}: Podaj liczbę naturalną: ")
  liczba_rzeczywista = bezpieczny_input_float(f"Liczba {n}: Podaj liczbę rzeczywistą: ")
  return Liczba(liczba_naturalna, liczba_rzeczywista)

liczba1 = liczba_z_input(1)
print()
liczba2 = liczba_z_input(2)
print()

print("Liczba 1: " + str(liczba1))
print("Liczba 2: " + str(liczba2))
print()

print("Liczba 1 * liczba 2:")
print(f"Wynik: {liczba1 * liczba2}")
print()

print("Liczba 1 @ liczba 2:")
print(f"Wynik: {liczba1 @ liczba2}")


# liczba1 = Liczba(3, 2.0)
# liczba2 = Liczba(5, 3.0)

# print(liczba1 * liczba2)
# print(liczba1 @ liczba2)

# print("Knuth 3↑↑3")
# print(knuth(3,2,3))

# knuth(8,2,3)

# dodatkowo: obliczanie strzałki knutha z zwiększonym stosem
# print("Knuth z większym stosem:")
# import threading
# threading.stack_size(2**26)
# t = threading.Thread(target=(lambda a,n,b: print(knuth(a,n,b))), args=(8,2,3))
# t.start()
# t.join()