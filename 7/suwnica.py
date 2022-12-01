# suwnica obsługująca plac kontenerowy

class TrzymaJużKontener(Exception):
    pass


class NieTrzymaKonteneru(Exception):
    pass


class SuwnicaJestZaWysoko(Exception):
    pass


class Suwnica:
    maksymalna_wysokosc = 9  # narzucone przez unię europerjską
    trzyma_kontener = False

    def __init__(self, pole_kontenerowe, x=0, z=0, y=0):
        self.pole_kontenerowe = pole_kontenerowe
        self.x = x
        self.y = y
        self.z = max(z, self.podaj_wysokosc_slupka(x, y) + 1)

    def podaj_wysokosc_slupka(self, x, y):
        return self.pole_kontenerowe[y][x]

    # travel to (x, y), step by step, using the shortest path
    def jedz(self, x, y):
        while self.x != x or self.y != y:
            if self.x < x:
                self.x += 1
            elif self.x > x:
                self.x -= 1
            if self.y < y:
                self.y += 1
            elif self.y > y:
                self.y -= 1
    
    def zlap(self):
        if self.trzyma_kontener:
            raise TrzymaJużKontener
        # sprawdź czy jest kontener pod suwnicą
        if self.pole_kontenerowe[self.y][self.x] == self.z + 1:
            self.pole_kontenerowe[self.y][self.x] -= 1
            self.trzyma_kontener = True
            return True
        elif self.pole_kontenerowe[self.y][self.x] < self.z + 1:
            raise SuwnicaJestZaWysoko

    def podnies(self, o_ile):
        # nie ma po co podnosić ponad max_wysokość + 1
        if self.z + o_ile >= self.maksymalna_wysokosc + 1:
            raise ValueError
        self.z += o_ile

    def opusc(self):
        if not self.trzyma_kontener:
            raise NieTrzymaKonteneru
        # Checking if the container is on top of another container. If it is, it is putting it down.
        if self.pole_kontenerowe[self.y][self.x] == self.z + 1:
            self.pole_kontenerowe[self.y][self.x] += 1
            self.trzyma_kontener = False
            return True
        elif self.pole_kontenerowe[self.y][self.x] < self.z + 1:
            raise SuwnicaJestZaWysoko(
                "Próbowano upuścić kontener z wysokości!")
            
    def __str__(self):
        # display the container field, with the number with the crane highlighted in yellow
        # under the crane, the coordinates of the crane are displayed
        output = "\n"
        for i in range(len(self.pole_kontenerowe)):
            for j in range(len(self.pole_kontenerowe[i])):
                if i == self.x and j == self.y:
                    output += "\033[33m\033[1m" + str(self.pole_kontenerowe[i][j]) + "\033[0m"
                else:
                    output += str(self.pole_kontenerowe[i][j])
                output += " "
            output += "\n"
        output += "---------\n"
        output += "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)
        return output

pole_kontenerowe = [
    [0, 4, 3, 2, 0],
    [3, 1, 0, 2, 5],
    [5, 0, 1, 3, 1],
]

suwnica = Suwnica(pole_kontenerowe)

print(suwnica)
print(suwnica.podaj_wysokosc_slupka(2, 0))
print(suwnica)
suwnica.jedz(2, 2)
print(suwnica)
