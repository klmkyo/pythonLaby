def ddd(x, epsilon=0.000001):
    """
    It computes the sum of the series
    
    until the absolute value of the next term is less than `epsilon`
    
    the code is optimized to avoid computing the factorial by using the
    fact that $(n+1)! = (n+1) n!$ and that $n! = n (n-1)!$ and so on
    
    :param x: the value of x to calculate the cosine of
    :param epsilon: the precision of the result
    :return: The value of the series
    """
    suma = 1
    an = 1
    n = 0
    while abs(an) > epsilon:
        an *= (-x * (2 * n-1)) / (2 * (n + 1))
        suma += an
        n += 1
    return suma
 
print(ddd(0.999))