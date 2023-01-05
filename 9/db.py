import struct
import hashlib

# change directory to script location
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# <name (25 chars)> <surname (34 chars)> <height [cm] (uint8 1B)> <weight [kg] (float 4B)>
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

# database file starts with one byte that indicates the status of transaction
# when starting writing to a file the first 4 bytes are set to the (index + 1) of the next person to be written
# when the write is successful the first byte is set to 0
# then the next 8 bytes is the cheksum of the file
class Database:
    people: list[Person]
    
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)
    
    def save_to_file(self, file):
        # set first byte to the index of the next person to be written
        file.write(struct.pack("I", len(self.people)))
        
        # move cursor to 12th byte
        file.seek(12)
        
        for person in self.people:
            person.write(file)
        
        # calculate and write checksum
        # use sha-1 algorithm and keep only 8 first bytes
        file.seek(12)
        checksum = hashlib.sha1(file.read(len(self.people) * 64)).digest()[:8]
        # print checksum in hex
        print(checksum.hex())
        file.seek(4)
        file.write(checksum)
                    
        # set first byte to 0
        file.seek(0)
        file.write(struct.pack("I", 0))
        file.flush()
    
    def __str__(self):
        return "\n".join([str(p) for p in self.people])
        
    @staticmethod
    def from_file(file):
        db = Database()
        # read first 4 bytes
        index = struct.unpack("I", file.read(4))[0]
        # if first 4 bytes is 0 then the file is corrupted
        if index != 0:
            raise Exception("File is corrupted (abanoned transaction)")
        # check the cheksum
        file.seek(4)
        file_checksum = file.read(8)
        
        file.seek(12)
        # read till the end of the file
        checksum = hashlib.sha1(file.read()).digest()[:8]
        # compare the checksums
        
        if checksum != file_checksum:
            raise Exception("File is corrupted (checksum)")
        
        # read all people
        file.seek(12)
        while True:
            try:
                person = Person.from_file(file)
                db.add(person)
            except struct.error:
                break
        return db
    

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

db = Database()

for i in range(10):
    p = Person(fake.first_name(), fake.last_name(), fake.random_int(100, 220), fake.pyfloat(min_value=40, max_value=120, right_digits=1))
    db.add(p)

with open("database.bin", "wb+") as f:
    db.save_to_file(f)
        
del db

db = Database.from_file(open("database.bin", "rb"))
print(db)
        
# Print all people
# [print(p) for p in people]