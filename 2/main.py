# BMI = waga / wzrost^2

while True:
    try:
        weight = float(input("Podaj swoją wagę [kg]: "))
        if(weight <= 0):
          print("Wartość nie może być ujemna!")
        elif(weight >= 800):
          print("Podana waga zbyt duża!")
        else:
          break
    except ValueError:
        print("Podana wartość nie jest liczbą!")

while True:
    try:
        height = float(input("Podaj swój wzrost [cm]: "))
        if(weight <= 0):
          print("Wartość nie może być ujemna!")
        else:
          break
    except ValueError:
        print("Podana wartość nie jest liczbą!")

print(f"Twoje BMI to: {weight/(height**2)}")
