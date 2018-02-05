from math import tan
from math import pi

def polysum(n, s):
    """ takes argument of _n_ number of sides and length _s_ of sides
    n : int
    s : int or float
        returns the sum of the area and the square of the perimeter
        precision is to 4 decimal places """
    
    areaPoly = (.25*n*s**2)/(tan(pi/n))
    periPoly = n*s
    
    floatSum = areaPoly + periPoly**2
    return float(format(floatSum, '.4f'))
