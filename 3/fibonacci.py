import functools

def fibonacci(n: int):
  if n == 0: return 0
  if n == 1 or n == 2: return 1
  
  a = 1
  b = 1
  for _ in range(2, n):
    c = a + b
    a = b
    b = c
  return b

@functools.lru_cache(maxsize=None)
def memo_fib(n: int):
  if n <= 1:
    return n
  else:
    return(memo_fib(n-1) + memo_fib(n-2))

fibonacci(100000)

# for i in range(0, 1000):
#   memo_fib(i)
