
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        s = self.side_length ** 2
        print (f'Площадь квадрата равна {s}')
        return s

    def perimeter(self):
        p = self.side_length * 4
        print (f'Периметр квадрата {p}')

class Triangle:
    def __init__(self, stopping_length,height):
        self.stopping_length = stopping_length
        self.height = height

    def area(self):
        s = self.stopping_length * self.height / 2
        print (f'Площадь треугольника равна {s}')
        return s

    def perimeter(self):
        p = self.height * 2 + self.stopping_length
        print (f'Периметр треугольника {p}')

class Cube(Square):
    # TODO,
    #  Вся поверхность 3D фигуры может храниться в виде списка, например для Куба это будет [Square, Square, Square, Square, Square, Square]
    #  По идее, куб должен содержать в одном из методе 6 классов Square. =)
    def area_cub(self):
       s = self.area() * 6
       print(f'площадь поверхности куба {s}')
       return s

# TODO, предлагаю попробовать добавить в решение класс Миксин
#  с одним методом - расчётом площади фигуры.



class Piramide(Triangle):
    def area_piramide(self):
       s = self.area() * 4 + self.stopping_length ** 2
       print (f'Площадь поверхности пирамиды {s}')
       return s

piramide = Piramide(5, 6)
piramide.area_piramide()