import math

class MyMath:

    def __init__(self):
        self.radius = None
        self.cube_side_length = None

    def circumference(self,radius):
        self.radius = radius
        return round(2 * radius * math.pi, 3)

    def area_circle(self,radius):
        return round(math.pi * radius**2,3 )

    def cube_volume(self,cube_side_length):
        return cube_side_length**3

    def sphere_area(self,radius):
        return round(4 * math.pi * radius ** 2)

res_1 = MyMath()
print(res_1.circumference(5))
res_2 = MyMath()
print (res_2.area_circle(6))

