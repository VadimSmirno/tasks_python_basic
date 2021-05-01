import math


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = int(radius)

    def area(self):
        area = math.pi * self.radius ** 2
        return area

    def perimeter(self):
        return 2 * math.pi * self.radius

    def big_circle(self, coefficient):
        return math.pi * self.radius ** 2 * coefficient

    # TODO, второй круг передавать в метод не нужно.
    #  Предлагаю сравнивать со "своими" аргументами =)
    #  через self.
    def crossing(self, circle):
        if isinstance(circle, Circle):
            d = math.sqrt((circle.x - circle2.x) ** 2 + (circle.y - circle2.y) ** 2)
            if d > (circle.radius + circle2.radius) or 0 < d < math.fabs(circle.radius - circle2.radius):
                print('общих точек нет')
            elif d == (circle.radius + circle2.radius) or d == math.fabs(circle.radius - circle2.radius):
                print('Есть одна общая точка')
            else:
                print('Есть две общие точки')


coefficient = int(input('Во сколько раз увеличить круг '))

circle1 = Circle(1, 2, 2)
circle2 = Circle(2, 4, 3)
print(circle1.perimeter())
print(circle1.big_circle(coefficient))
circle1.crossing(circle1)
