import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health_1 = 100
        # TODO, у одного война должен быть только 1 показатель здоровья.
        self.health_2 = 100

    def fight(self):
        # TODO, по идее, этот метод должен принимать на вход объект Warrior
        #  Проверять, является ли он объектом класса Warrior и наносить урон ему, а не себе.
        #  Давайте немного поправим.
        #  Цикл с боем должен быть вне этого метода.
        while self.health_1 > 0 and self.health_2 > 0:
            who_hits = random.randint(1, 2)
            if who_hits == 1:
                self.health_2 -= 20
                print(f'Бьет {warrior_1.name}    у {warrior_2.name} осталось {self.health_2} HP')
            elif who_hits == 2:
                self.health_1 -= 20
                print(f'Бьет {warrior_2.name}    у {warrior_1.name} осталось {self.health_1} HP')


warrior_1 = Warrior('Воин 1')
warrior_2 = Warrior('Воин 2')
warrior_2.fight()
