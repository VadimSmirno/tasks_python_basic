import math

class MyMath:

    @classmethod
    def circumference(cls,radius):

        return round(2 * radius * math.pi, 3)
    @classmethod
    def area_circle(cls,radius):
        return round(math.pi * radius**2,3 )

    @classmethod
    def cube_volume(cls,cube_side_length):
        return cube_side_length**3

    @classmethod
    def sphere_area(cls,radius):
        return round(4 * math.pi * radius ** 2)

res_1 = MyMath.circumference(5)
print(res_1)
res_2 = MyMath.area_circle(6)
print (res_2)

