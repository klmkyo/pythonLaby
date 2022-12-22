import os


def kopiuj(zrodlo, cel):
    with open(zrodlo, "rb") as wejscie:
        with open(cel, "wb") as wyjscie:
            while True:
                bufor = wejscie.read(1024)
                if not bufor:
                    break
                wyjscie.write(bufor)


def jedna_linia(zrodlo, cel):
    with open(zrodlo, "r") as wejscie:
        with open(cel, "w") as wyjscie:
            while True:
                linia = wejscie.readline()
                if not linia:
                    break
                wyjscie.write(linia.rstrip("\n"))


# ask user for input and output file names, check if input exists
f1 = input("Podaj nazwę pliku źródłowego: ")
f2 = input("Podaj nazwę pliku docelowego: ")

if not os.path.exists(f1):
    print("Plik źródłowy nie istnieje!")
    exit(1)

jedna_linia(f1, f2)
