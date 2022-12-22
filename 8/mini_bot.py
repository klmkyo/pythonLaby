import random

class MiniBot:
  __ZAKRES_CZESTOTLIWOSCI = (100, 200)
  __czestotliwosc = 150
  __w_ruchu = False
  
  __suma_pomiarow = 0
  __liczba_pomiarow = 0
  
  def __init__(self, cz_min=100, cz_max=200, cz_domyslna=150):
    self.__ZAKRES_CZESTOTLIWOSCI = (cz_min, cz_max)
    self.__czestotliwosc = cz_domyslna if cz_domyslna in range(self.__ZAKRES_CZESTOTLIWOSCI) else cz_min
  
  def jedz(self):
    self.__w_ruchu = True
    print("Jedzie...")
  
  def zatrzymaj(self):
    self.__w_ruchu = False
    print("Zatrzymano")
  
  def ustaw_czestotliwosc(self, czestotliwosc: float):
    # sprawdz czy czestotliwosc jest w zakresie
    if czestotliwosc not in range(self.__ZAKRES_CZESTOTLIWOSCI):
      raise ValueError(f"Zakres {czestotliwosc} jest poza zakresem {self.__ZAKRES_CZESTOTLIWOSCI}")
    print(f"Ustawiono czestotliwosc na {czestotliwosc} Hz")
    self.__czestotliwosc = czestotliwosc
  
  def podaj_wartosc_promieniowania(self):
    # można mierzyć jedynie w postoju
    if self.__w_ruchu:
      raise RuntimeError("Nie można mierzyć w ruchu")
    # tani chiński sensor
    pomiar = random.randint(0, 100)
    __suma_pomiarow += pomiar
    
    return 
  

botlist = [MiniBot() for _ in range(10)]
pomiary = []

for bot in botlist:
  pomiary.append(bot.podaj_wartosc_promieniowania())

print(pomiary)