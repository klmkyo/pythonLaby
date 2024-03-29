def schemat_hornera(x, lista_a: list[float]):
    """ n-ty stopien jest wyczytywany z długości lista_a """
    wyn = lista_a[0]

    for i in range(1, len(lista_a)):
        wyn = wyn*x + lista_a[i]

    return wyn

def pochodna_schemat_hornera(x, lista_a: list[float]):
    """ n-ty stopien jest wyczytywany z długości lista_a """
    wyn = lista_a[0]

    for i in range(1, len(lista_a) - 1):
        wyn = wyn*x*(i+1) + lista_a[i]
        
    return wyn

def miejsce_zerowe(start, lista_a: list[float], epsilon=0.0001):
    xn = start
    # setting roznica to epsilon + 1 to enter the loop
    roznica = epsilon + 1
    
    while abs(roznica) >= epsilon:
        print(xn)
        gora = schemat_hornera(xn, lista_a)
        pochodna = pochodna_schemat_hornera(xn, lista_a)
        if pochodna == 0: 
            xn = (xn + gora)/2
            continue
        roznica = (gora/pochodna)
        xn = xn - roznica

    return xn 

print(miejsce_zerowe(-2, [2,-2,-3]))