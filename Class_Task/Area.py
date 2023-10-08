import math


def area(radius):
    if radius < 0:
        raise ValueError("Radius cannot not be a negative number")
    if type(radius) != float and type(radius) != int:
        raise TypeError("Data type is wrong")

    return math.pi * (radius ** 2)


area(4)
