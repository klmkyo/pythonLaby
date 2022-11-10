from cmath import pi

def pole_okregu(r: float):
  return (r*r) * pi

r = float(input("Podaj promień okręgu: "))
print(f"Pole okręgu o promieniu {r} wynosi {pole_okregu(r)}")