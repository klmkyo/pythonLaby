
suma_ocen = 0
i = 0

while True:
  inp = input("Podaj ocenę, lub wpisz q żeby zakończyć: ")
  
  if inp == "q":
    break
  
  try:
    ocena = int(inp)
    if(ocena < 1 or ocena > 6):
      print("Ocena nie jest w prawidłowym zakresie 1-6")
      continue
    
    print(f"Dodawanie {ocena} do ocen")
    suma_ocen += ocena
    i += 1
    
  except ValueError:
    print("Podano nieprawidłową wartość")

if(i == 0):
  print("Podano 0 ocen")
  exit(1)

print(f"Średnia to: {suma_ocen/i}")