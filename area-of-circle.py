import math

def area_of_circle(r):
    area = math.pi * pow(r, 2)
    return area

circle = area_of_circle(5)
print(f"Area of circle is {round(circle, 2)}")