min = float("-inf")
max = min
drugiemax = min

while True:
  
  inp = input("Podaj liczbę, lub wpisz q żeby zakończyć: ")
  
  if inp == "q":
    break
  
  try:
    ocena = float(inp)
    
    if ocena > max:
      drugiemax = max
      max = ocena
    elif ocena > drugiemax and ocena < max:
      ocena = drugiemax
    
  except ValueError:
    print("Podano nieprawidłową wartość")

print()
if(drugiemax != min): print(f"Druga największa: {drugiemax}")
if(max != min): print(f"Największa: {max}")