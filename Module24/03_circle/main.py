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

    def crossing(self, circle):
        if isinstance(circle, Circle):

            d = math.sqrt((circle.x - self.x) ** 2 + (circle.y - self.y) ** 2)
            if d > (circle.radius + self.radius) or 0 < d < math.fabs(circle.radius - self.radius):
                print('общих точек нет')
            elif d == (circle.radius + self.radius) or d == math.fabs(circle.radius - self.radius):
                print('Есть одна общая точка')
            else:
                print('Есть две общие точки')


coefficient = int(input('Во сколько раз увеличить круг '))

circle1 = Circle(1, 2, 2)
circle2 = Circle(2, 4, 3)
circle1.crossing(circle2)

# зачёт!
