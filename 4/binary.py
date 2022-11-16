from math import sin

def funkc(x: float):
  return sin(x)

def miejsceZerowe(f, lewo, prawo, eps):
  if(f(lewo) * f(prawo) > 0):
    return None
  
  srodek = None
  
  while(prawo - lewo > eps):
    srodek = (lewo + prawo) / 2
    
    f_srodek = f(srodek)
    if f_srodek == 0:
      return srodek
    # gdy miejsce zerowe jest po lewej stronie
    elif(f(lewo) * f_srodek < 0):
      prawo = srodek
    # gdy miejsce zerowe jest po prawej stronie
    else:
      lewo = srodek
      
      
  return srodek

print(miejsceZerowe(sin, -1, 1, 0.0000000001))
print(miejsceZerowe(sin, 1, 4, 0.0000000001))
print(miejsceZerowe(sin, 4, 7, 0.0000000001))