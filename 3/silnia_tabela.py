import functools
from re import I
import sys

sys.set_int_max_str_digits(999999999)

def silnia(x: int):
  if(x == 0): return 1
  a = 1
  for i in range(2, x + 1):
    a *= i
  return a

@functools.lru_cache(maxsize=None)
def memo_silnia(x: int):
  if(x == 0): return 1
  return x * memo_silnia(x - 1)

for i in range(0,10000):
  print(f"{i}: {memo_silnia(i)}")