from math import sin

def funkc(x: float):
  return sin(x)

def miejsceZerowe(f, lewo, prawo, eps):
  if(f(lewo) * f(prawo) > 0):
    return None
  
  while(prawo - lewo > eps):
    srodek = (lewo + prawo) / 2
    
    f_srodek = f(srodek)
    if f_srodek == 0:
      return srodek
    elif(f(lewo) * f_srodek < 0):
      prawo = srodek
    else:
      lewo = srodek
  return (lewo + prawo) / 2

print(miejsceZerowe(funkc, -1, 1, 0.00001))