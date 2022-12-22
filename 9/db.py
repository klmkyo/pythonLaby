import struct

# change directory to script location
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# <name (25 chars)> <surname (34 chars)> <height [cm] (uint_8 1B)> <weight [kg] (float 4B)>
class Person:
    name: str
    surname: str
    height: int
    weight: float

    def __init__(self, name, surname, height, weight):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.surname} {self.height} {self.weight}"

    def write(self, file):
        b_name = self.name.encode()
        b_surname = self.surname.encode()

        data = struct.pack("25s 34s B f", b_name, b_surname, self.height, self.weight)
        file.write(data)
    
    @staticmethod
    def from_file(file):
        name, surname, height, weight = struct.unpack("25s 34s B f", file.read(64))
        return Person(name.decode().rstrip("\0"), surname.decode().rstrip("\0"), height, round(weight, 1))

### Manualne tworzenie osoby

# jan = Person("Jan", "Kowalski", 180, 80.5)
# print(jan)
# with open("plik.bin", "wb") as plik:
#     jan.write(plik)
    
# del jan
# jan2 = Person.from_file(open("plik.bin", "rb"))
# print(jan2)



### Tworzenie 1000 osób z losowymi danymi i zapis do pliku

from faker import Faker
fake = Faker(locale="pl_PL")
with open("database.bin", "wb") as f:
    for i in range(1000):
        p = Person(fake.first_name(), fake.last_name(), fake.random_int(100, 220), fake.pyfloat(min_value=40, max_value=120, right_digits=1))
        p.write(f)
        
# Read all people from file
people: list[Person] = []
with open("database.bin", "rb") as f:
    while True:
        try:
            person = Person.from_file(f)
            people.append(person)
            print(person)
        except struct.error:
            break
        
# Print all people
# [print(p) for p in people]