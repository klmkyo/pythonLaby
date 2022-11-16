import sys

sys.set_int_max_str_digits(999999999)

def silnia(x: int):
  if(x == 0): return 1
  a = 1
  for i in range(2, x + 1):
    a *= i
  return a

print(silnia(6))