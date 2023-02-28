import random
import time


def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

# create a 5000 element list of random numbers
arr = [random.randint(0, 100) for _ in range(10 ** 5)]

@timeit
def reverse_list_swap(arr: list):
  for n in range(len(arr) // 2):
    arr[n], arr[-n-1] = arr[-n-1], arr[n]
    
    
# print(arr)
reverse_list_swap(arr)
# print(arr)

print()