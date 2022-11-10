import math

# do obliczenia

def funkc(x):
  s = 1
  n = 1
  while True:
    res = ((1 - (2*n)) * x) / 2*(n+1)
    s += res
    n += 1
    if res < 0.001 and res > -0.001:
      return s

print(funkc(0.999))