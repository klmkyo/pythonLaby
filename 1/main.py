# BMI = waga / wzrost^2

weight = float(input("Podaj swoją wagę: "))
height = float(input("Podaj swój wzrost [cm]: ")) / 100

print(f"Twoje BMI to: {weight/(height**2)}")
