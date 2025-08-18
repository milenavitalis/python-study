from math import pi, sqrt
from newmodule import saudation, double 

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * (radius ** 2)

print("Circle area with radius 5:", calculate_circle_area(5))

def square_root(numero):
    if numero < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return sqrt(numero)

print("Square root of 16:", square_root(16))

print("Boas vindas:", saudation("Milena"))
print("Dobro de 4:", double(4))