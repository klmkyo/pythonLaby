# suwnica obsługująca plac kontenerowy

class TrzymaJużKontener(Exception):
  pass

class NieTrzymaKonteneru(Exception):
  pass

class SuwnicaJestZaWysoko(Exception):
  pass

class Suwnica:
  maksymalna_wysokosc = 9 # narzucone przez unię europerjską
  trzyma_kontener = False
  
  def __init__(self, pole_kontenerowe, x=0, z=0, y=0):
    self.pole_kontenerowe = pole_kontenerowe
    self.x = x
    self.z = z
    self.y = max(y, self.podaj_wysokosc_slupka(x, z) + 1)

  def podaj_wysokosc_slupka(self, x, z):
    return self.pole_kontenerowe[x][z]
  
  # x, y to miejsce docelowe
  def jedz(self, x, y):
    return None
  
  def zlap(self):
    if self.trzyma_kontener:
      raise TrzymaJużKontener
    # sprawdź czy jest kontener pod suwnicą
    if self.pole_kontenerowe[self.x][self.z] == self.y + 1:
      self.pole_kontenerowe[self.x][self.z] -= 1
      self.trzyma_kontener = True
      return True
    elif self.pole_kontenerowe[self.x][self.z] < self.y + 1:
      raise SuwnicaJestZaWysoko
  
  def podnies(self, o_ile):
    # nie ma po co podnosić ponad max_wysokość + 1
    if self.y + o_ile >= self.maksymalna_wysokosc + 1:
      raise ValueError
    self.y += o_ile

  def opusc(self):
    if not self.trzyma_kontener:
      raise NieTrzymaKonteneru
    if self.pole_kontenerowe[self.x][self.z] == self.y + 1:
      self.pole_kontenerowe[self.x][self.z] += 1
      self.trzyma_kontener = False
      return True
    elif self.pole_kontenerowe[self.x][self.z] < self.y + 1:
      raise SuwnicaJestZaWysoko("Próbowano upuścić kontener z wysokości!")
      

pole_kontenerowe = [
  [0, 4, 3, 2, 0],
  [3, 1, 0, 2, 5],
  [2, 0, 1, 3, 1],
]

