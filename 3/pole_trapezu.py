
def pole_trapezu(a: float, b: float, h: float):
  return ((a + b) / 2) * h

a = float(input("Podaj długość podstawy a: "))
b = float(input("Podaj długość podstawy b: "))
h = float(input("Podaj wysokość trapezu: "))
print(f"Pole trapezu o podstawach {a} i {b} oraz wysokości {h} wynosi {pole_trapezu(a, b, h)}")