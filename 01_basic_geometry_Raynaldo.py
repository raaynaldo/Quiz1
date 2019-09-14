import math
base = float(input("base : "))
base1 = float(input("base1 : "))
base2 = float(input("base2 : "))
height = float(input("height : "))
side_length = float(input("side_length : "))
radius = float(input("radius : "))

print("Area of a Rectangle: ", base * height)
print("Area of a Square: ", side_length**2)
print("Area of Triangle: ", (base * height)/2)
print("Area of Parallelogram: ", base * height)
print("Area of Trapezoid: ", (base1 * base2)/2*height)
print("Area of Circle: ", math.pi*(radius**2))