n = int(0)  # stopien wiel; podawany przez użytkownika
a = list()  # współczynniki wielomianu od najwyższego; podawane przez użytkownika
aprim = list()  # współczynniki pochodnej wielomianu (czyli też wielomianu) od najwyższego; obliczane


def wielomian(x, a, n):  # policzony schematem Hornera
    y = a[0]
    for i in range(n):
        y = y * x + a[i + 1]
    return y

def qqf(x):
    # global a, n Z TEGO SIĘ WYTŁUMACZĘ NA WYKŁADZIE;) - PROSZE MI PRZYPOMNIEĆ, GDYBYM TEGO NIE ZROBIŁ NA WSTĘPIE
    return wielomian(x, a, n)

def qqfprim(x):
    # global aprim, n
    return wielomian(x, aprim, n - 1)

def met_stycz(x, eps, f, fprim):  # przy wywołaniu fprim( x ) musi być różne od 0

    xn2 = x
    xn1 = x + 2 * eps
    while abs(xn2 - xn1) >= eps:
        xn0 = xn1
        xn1 = xn2
        y = fprim(xn1)
        if y != 0:
            xn2 = xn1 - f(xn1) / y
        else:
            xn2 = (xn1 + xn0) / 2
    return xn2


'''
    # wczytanie danych Z TEGO HASH'A TEŻ SIĘ MAM WYTŁUMACZYĆ
'''
n = int(input('podaj stopień wielomianu:'))
for i in range(n+1):
    x = float(input(f'podaj współczynnik wielomianu przy { n- i } potędze:'))
    a.append(x)
x = float(input('podaj punkt startowy:'))
dok = float(input('podaj dokładność metody:'))
'''
    # obliczenie współczynników pochodnej wielomianu
'''
for i in range(n):
    aprim.append((n - i) * a[i])
'''
'''
print(met_stycz(x, dok, qqf, qqfprim))
