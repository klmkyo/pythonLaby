import random

class MiniBot:
  zakres_czestotliwosci = (100, 200)
  czestotliwosc = 150
  w_ruchu = False
  
  def jedz(self):
    self.w_ruchu = True
    print("Jedzie...")
  
  def zatrzymaj(self):
    self.w_ruchu = False
    print("Zatrzymano")
  
  def ustaw_czestotliwosc(self, czestotliwosc: float):
    # sprawdz czy czestotliwosc jest w zakresie
    if czestotliwosc < self.zakres_czestotliwosci[0] or czestotliwosc > self.zakres_czestotliwosci[1]:
      raise ValueError(f"Zakres {czestotliwosc} jest poza zakresem {self.zakres_czestotliwosci}")
    print(f"Ustawiono czestotliwosc na {czestotliwosc} Hz")
    self.czestotliwosc = czestotliwosc
  
  def podaj_wartosc_promieniowania(self):
    # można mierzyć jedynie w postoju
    if self.w_ruchu:
      raise ValueError("Nie można mierzyć w ruchu")
    # tani chiński sensor
    return random.randint(0, 100)
  