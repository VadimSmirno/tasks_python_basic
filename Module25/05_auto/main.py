import math


class Car:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance):
        new_x = self.x + distance * math.cos(math.radians(self.angle))
        new_y = self.y + distance * math.sin(math.radians(self.angle))
        print(f'Автомобиль переехал. Новые координаты X = {new_x} Y = {new_y}')

    def to_turn(self, angle_of_rotation):
        print(f'Меняем направление на угол {angle_of_rotation + self.angle} ')


class Bus(Car):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.passengers = 0
        self.money = 0

    def come_in(self):
        if self.passengers < 40:
            self.passengers += 1
        print(f'В автобусе {self.passengers} человек')
        return self.passengers

    def go_out(self):
        if self.passengers >= 1:
            self.passengers -= 1
        print(f'В автобусе {self.passengers} человек')
        return self.passengers

    def move(self, distance):
        self.money += distance * 5 * self.passengers  # 5 рублей с км пути
        print(f'Заработано денег {self.money}')

# зачёт!
