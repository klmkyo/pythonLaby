# class Kierunki:
#     GORA = (0, -1)
#     DOL = (0, 1)
#     LEWO = (-1, 0)
#     PRAWO = (1, 0)

# suwnica obsługująca plac kontenerowy


class TrzymaJużKontener(Exception):
    pass
class NieTrzymaKonteneru(Exception):
    pass
class SuwnicaJestZaWysoko(Exception):
    pass

class Suwnica:
    maksymalna_wysokosc = 10  # narzucone przez unię europerjską
    trzyma_kontener = False

    def __init__(self, pole_kontenerowe, x=0, y=0, z=0):
        self.pole_kontenerowe = pole_kontenerowe
        self.x = x
        self.y = y
        self.z = max(z, self.ile(x, y) + 1)

        print(
            f"Ustawiono suwnicę na pozycji x: {self.x}, y: {self.y}, z: {self.z}")

    def ile(self, x, y):
        return self.pole_kontenerowe[y][x]

    # travel to (x, y), step by step, using the shortest path
    def jedz(self, x, y, z=None):
        """Przesuwa suwnicę do x, y, podnasząc przy tym suwnicę jeśli konieczne. 
        Jeśli podano z, to suwnica zostanie dodatkowo przesunięta do poziomu z."""

        print(f"\n\nTransportowanie suwnicy do x: {x}, y: {y}, z: {z}")
        while self.x != x or self.y != y:
            nowe_x = self.x
            nowe_y = self.y
            if self.x < x:
                nowe_x += 1
            elif self.x > x:
                nowe_x -= 1
            elif self.y < y:
                nowe_y += 1
            elif self.y > y:
                nowe_y -= 1
            
            # jeśli jest przeszkoda na drodze, to podnieś suwnicę
            if self.pole_puste(nowe_x, nowe_y, self.z):
                self.x = nowe_x
                self.y = nowe_y
                
                print(self)
                if self.x < x:
                    print("Przesunięto suwnicę w prawo...")
                elif self.x > x:
                    print("Przesunięto suwnicę w lewo...")
                elif self.y < y:
                    print("Przesunięto suwnicę w dół...")
                elif self.y > y:
                    print("Przesunięto suwnicę w górę...")
            else:
                self.podnies(1)
                print(
    f"Napotkano przeszkodę na drodze! (x: {nowe_x}, y: {nowe_y}, z: {self.z})")

        # jeśli podano z, to przenieś suwnicę do z
        if z is not None:
            print(f"Przewuanie suwnicy do poziomu z: {z}")
            if self.pole_puste(x, y, z):
                while self.z != z:
                    if self.z < z:
                        self.podnies(1)
                    elif self.z > z:
                        self.opusc(1)
            else:
                raise ValueError("Nie można ustawić suwnicy na tym poziomie!")
        print(
f"Suwnica została przesunięta do pozycji x: {self.x}, y: {self.y}, z: {self.z}!")

    # sprawdza czy pole jest puste

    def pole_puste(self, x, y, z):
        # print(f"POLE_PUSTE_CHECK x: {x}, y: {y}, z: {z} wysokść: {self.podaj_wysokosc_slupka(x, y)}")
        return self.ile(x, y) < z

    def zlap_kontener(self):
        if self.trzyma_kontener:
            raise TrzymaJużKontener
        
        # sprawdź czy jest kontener pod suwnicą
        if self.z - 1 > self.pole_kontenerowe[self.y][self.x]:
            raise SuwnicaJestZaWysoko
        
        self.pole_kontenerowe[self.y][self.x] -= 1
        self.trzyma_kontener = True
        print("Złapano kontener!")
        return True

    def pusc_kontener(self):
        if not self.trzyma_kontener:
            raise NieTrzymaKonteneru
        
        # sprawdź czy wysokość jest odpowiednia
        if self.z - 2 > self.pole_kontenerowe[self.y][self.x]:
            raise SuwnicaJestZaWysoko(
                "Próbowano upuścić kontener z wysokości!")
            
        self.pole_kontenerowe[self.y][self.x] += 1
        self.trzyma_kontener = False
        print("Puszczono kontener!")
        return True

    def podnies(self, o_ile):
        docelowe_z = self.z + o_ile

        # nie ma po co podnosić ponad max_wysokość + 1
        if docelowe_z >= self.maksymalna_wysokosc + 1:
            raise ValueError(
                "Próbowano podnieść suwnicę ponad maksymalną wysokość!")

        while self.z != docelowe_z:
            self.z += 1
            print(self)
            print(f"Podniesiono suwnicę...")

    def opusc(self, o_ile):
        docelowe_z = self.z - o_ile
        
        bezpieczne_z = docelowe_z + 1 if self.trzyma_kontener else docelowe_z
        
        if not self.pole_puste(self.x, self.y, bezpieczne_z):
            raise ValueError("Na podanym poziomie znajduje się kontener!")

        while self.z != docelowe_z:
            self.z -= 1
            print(self)
            print(f"Opuszczono suwnicę...")

    def __str__(self):
        output = "\n\n"
        for i in range(len(self.pole_kontenerowe)):
            for j in range(len(self.pole_kontenerowe[i])):
                if j == self.x and i == self.y:
                    output += "\033[33m\033[1m" + \
                        str(self.pole_kontenerowe[i][j]) + "\033[0m"
                else:
                    output += str(self.pole_kontenerowe[i][j])
                output += " "
            output += "\n"
        output += "---------\n"
        output += "> Trzyma kontener: " + str(self.trzyma_kontener) + "\n"
        output += "> x: " + str(self.x) + " y: " + \
            str(self.y) + " z: " + str(self.z)
        return output

def widocznosc_miedzy_kontenerami(suwnica: Suwnica, x1, y1, x2, y2, h):
    if x1 == x2:
        smaller_y = min(y1, y2)
        bigger_y = max(y1, y2)
        for i in range(smaller_y + 1, bigger_y):
            if suwnica.ile(x1, i) > h:
                return False
    elif y1 == y2:
        smaller_x = min(x1, x2)
        bigger_x = max(x1, x2)
        for i in range(smaller_x + 1, bigger_x):
            if suwnica.ile(i, y1) > h:
                return False
    else:
        raise ValueError("Nie można sprawdzić widoczności między dwoma punktami, które nie są na jednej linii!")
    return True

pole_kontenerowe = [
    [0, 4, 3, 2, 0],
    [3, 1, 0, 2, 5],
    [5, 0, 7, 5, 1],
]

# koordynaty x, y zaczynają się od 0
# suwnica musi być nad kontenerem aby go złapać

suwnica = Suwnica(pole_kontenerowe, 0, 0)

print(suwnica)
suwnica.jedz(2, 2)
suwnica.jedz(4, 2, 2)
suwnica.zlap_kontener()
suwnica.jedz(4, 0, 2)
suwnica.pusc_kontener()
print(suwnica)

print(f"Widoczność między punktami (x:0, y:1) oraz (x:4, y:1) na wysokości 2: {widocznosc_miedzy_kontenerami(suwnica, 0, 1, 4, 1, 2)}")
print(f"Widozność między punktami (x:0, y:2) oraz (x:3, y:2) na wysokości 6: {widocznosc_miedzy_kontenerami(suwnica, 0, 2, 3, 2, 6)}")
