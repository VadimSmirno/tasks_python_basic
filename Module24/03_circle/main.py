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

    # TODO, метод должен принимать на вход параметр - другой круг и далее, в коде работать с ним.
    #  про переменные сircle2 и сircle1 класс по идее ничего не знает.
    #  Если их не создать, получим ошибку.
    #  Класс должен работать со своими аргументами и аргументами того объекта, который передаём в метод crossing
    def crossing(self):
        if isinstance(сircle2 and сircle1, Circle):
            d = math.sqrt((сircle1.x - сircle2.x) ** 2 + (сircle1.y - сircle2.y) ** 2)
            if d > (сircle1.radius + сircle2.radius) or 0 < d < math.fabs(сircle1.radius - сircle1.radius):
                print('общих точек нет')
            elif d == (сircle1.radius + сircle2.radius) or d == math.fabs(сircle1.radius - сircle1.radius):
                print('Есть одна общая точка')
            else:
                print('Есть две общие точки')


coefficient = int(input('Во сколько раз увеличить круг '))

сircle1 = Circle(1, 2, 2)
сircle2 = Circle(20, 40, 1)
print(сircle1.perimeter())
print(сircle1.big_circle(coefficient))
сircle1.crossing()
