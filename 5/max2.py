n = int(input('ile liczb? '))  # sprawdzić, czy n poprawne
x = float(input('podaj liczbę: '))

mx2 = mx = x
# Checking if the number is bigger than the previous number.
for i in range(n - 1):
    x = float(input('podaj liczbę: '))
    if x > mx:
        mx2 = mx
        mx = x
    elif x < mx:
        if x > mx2 or mx == mx2:
            mx2 = x
        
print(f'Największa liczba to {mx}')
if mx == mx2:
    print('nie ma drugiego max')
else:
    print('drugie max to:', mx2)
