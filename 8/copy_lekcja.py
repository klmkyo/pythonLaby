p1 = open("plik1.txt", "r")
p2 = open("plik2.txt", "w")

linia = p1.readline()
while linia != "":
    p2.write(linia[:-1])
    linia = p1.readline()