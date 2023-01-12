from pprint import pprint


def func(arr: list):
  # int: int dictionary
  counts: dict[int, int] = {}
  for n in arr:
    if n in counts:
      counts[n] += 1
    else:
      counts[n] = 1
  
  sorted_keys = sorted(counts.keys())
  first = sorted_keys[0]
  last = sorted_keys[-1]
  
  # wypełnianie kluczy pomiędzy
  for i in range(first, last + 1):
    counts[i] = counts.get(i, 0)
  print_dict_sorted(counts)
  
  
  lastval = counts[first] - 1
  temp_arr: list[int] = [lastval]
  for i in range(first + 1, last + 1):
    newval = counts[i] + lastval
    temp_arr.append(newval)
    lastval = newval
    
  print("\ntemp_arr:")
  print(temp_arr)
  
  results: list[int] = [None] * len(arr)
  for i in range(len(arr) - 1, -1, -1):
    n = arr[i]
    results[temp_arr[n]] = n
    temp_arr[n] -= 1
    # print(temp_arr)
      
  print("\nresults:")
  print(results)
  return results
    

def print_dict_sorted(d: dict):
  # sort by keys
  for k in sorted(d.keys()):
    print(f"{k}: {d[k]}")

arr = [2, 5, 7, 0, 3, 2, 5, 6, 2, 0, 1]
func(arr)