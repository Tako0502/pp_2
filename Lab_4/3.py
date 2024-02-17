import math
def deg2rad(deg):
    return deg * (math.pi / 180)



 #-------------------------Tasks---------------------------
def trapezoidalArea(h , a, b):
    s = ((a + b)*h) / 2
    return s

h,a,b= 5,5,6
s=trapezoidalArea(h,a,b)
print(s)

 #-------------------------Tasks---------------------------


def area_of_regular_polygon(n, s):
    return (1 / 4) * n * s ** 2 * (1 / math.tan(math.pi / n))

num_sides = 4  
side_length = 25 
area = area_of_regular_polygon(num_sides, side_length)
print(int(area))


def area_of_parallelogram(a,h):
    return a*h

 #-------------------------Tasks---------------------------
