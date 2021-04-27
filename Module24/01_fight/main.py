import random

class Warrior:

    def __init__(self,name, health):
        self.name = name
        self.health = health

    def print_info(self,name):
        if not isinstance(name, Warrior):
            self.health -= 20

        print (f'Бьет {self.name} у противника осталось здоровья {self.health}')
        return self.health

warrior_1 = Warrior('Воин 1',100)
warrior_2 = Warrior('Воин 2',100)
warrior1 = 1
warrior2 = 1
while warrior1 > 0 and warrior2 > 0:
    who_hits = random.randint(1, 2)
    if who_hits == 1:
        warrior1 = warrior_1.print_info(warrior_1.name)
    else:
        warrior2 = warrior_2.print_info(warrior_2.name)
else:
    if warrior1 > warrior2:
        print (f'\nПобедил {warrior_1.name}, у него осталось {warrior_1.health} едениц здоровья')
    else:
        print(f'\nПобедил {warrior_2.name}, у него осталось {warrior_2.health} едениц здоровья')