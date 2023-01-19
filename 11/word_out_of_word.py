
def can_be_made(dest: str, origin: str):
  letters: dict[str, int] = {}
  
  for char in origin:
    if char in letters:
      letters[char] += 1
    else:
      letters[char] = 1
      
  for char in dest:
    if char in letters:
      letters[char] -= 1
    else:
      return False
    
  for k in letters.keys():
    if letters[k] < 0:
      return False
  
  return True

# test cases
word_pairs: list[tuple[str, str]] = [
  ("hello", "ehllo"),
  ("world", "wrld"),
  ("test_123", "32t"),
  ("32t", "test_123"),
]

for pair in word_pairs:
  print(f"{pair[0]} can be made from {pair[1]}: {can_be_made(pair[0], pair[1])}")