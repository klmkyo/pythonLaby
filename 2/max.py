
liczba = None

while True:
  try:
    liczba = float(input("Podaj liczbę: "))
    break
  except ValueError:
    print("To nie jest liczba!")
    
max = drugiemax = liczba

while True:
  
  inp = input("Podaj liczbę, lub wpisz q żeby zakończyć: ")
  
  if inp == "q":
    break
  
  try:
    liczba = float(inp)
    
    if liczba > max:
      drugiemax = max
      max = liczba
    elif liczba > drugiemax and liczba < max:
      drugiemax = liczba
      
  except ValueError:
    print("To nie jest liczba!")

print()

if(drugiemax != max): print(f"Druga największa: {drugiemax}")
print(f"Największa: {max}")