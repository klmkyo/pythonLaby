def schemat_hornera(x, lista_a: list[float]):
    """ n-ty stopien jest wyczytywany z długości listy a """
    wyn = lista_a[0]

    for i in range(0, len(lista_a) - 1):
        wyn = wyn*x + lista_a[i]

    return wyn

def pochodna_schemat_hornera(x, lista_a: list[float]):
    """ n-ty stopien jest wyczytywany z długości listy a """
    wyn = lista_a[0]

    for i in range(0, len(lista_a) - 2):
        wyn = wyn*x*(i+1) + lista_a[i]
        
    return wyn

def miejsce_zerowe(start, lista_a: list[float], epsilon=0.0001):
    xn = start

    while abs(xn) >= epsilon:
        print(xn)
        gora = schemat_hornera(xn, lista_a)
        pochodna = pochodna_schemat_hornera(xn, lista_a)
        if pochodna == 0: 
            xn = (xn + gora)/2
            continue

        xn = xn - (gora/pochodna)

    return xn 

print(miejsce_zerowe(-2, [1,-2,-3]))