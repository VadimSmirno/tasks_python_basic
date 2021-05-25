
class Square:
    def __init__(self, side_length):
        self.side_length = side_length


    def perimeter(self):
        p = self.side_length * 4
        print (f'Периметр квадрата {p}')

class Triangle:
    def __init__(self, stopping_length,height):
        self.stopping_length = stopping_length
        self.height = height


    def area(self):
        s = self.stopping_length * self.height / 2
        return s

    def perimeter(self):
        p = self.height * 2 + self.stopping_length
        print (f'Периметр треугольника {p}')

class Mixsin:
    def area_mixsin(self,side_length):
        self.side_length = side_length
        s = self.side_length ** 2
        return s

class Cube(Square,Mixsin):

    def area_cub(self):
       lst = [Square, Square, Square, Square, Square, Square]
       return lst

class Piramide(Triangle,Mixsin):
    def area_piramide(self):
       lst = [Triangle,Triangle,Triangle,Triangle,Mixsin]
       return lst

piramide = Piramide(5, 6)
piramide.area_piramide()
cub = Cube(6)
cub.area_cub()
res = 0
for i_class in piramide.area_piramide():
    try:
        res += i_class(stopping_length=5,height=6).area()
    except Exception:
        res += i_class().area_mixsin(side_length=4)
print (f'Площадь фигуры {res}')