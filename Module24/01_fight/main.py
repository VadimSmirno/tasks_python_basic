import random

class Warrior:

    def __init__(self,name, health):
        self.name = name
        self.health = health

    def print_info(self,name_warrior,hp):
        if isinstance(name_warrior, Warrior):
            # TODO, стоит переименовать name. Это ведь "другой воин"?
            # TODO, стоит поправить условие.
            #  Если "другой воин" является Warrior, то стоит отнимать health у него.
            hp -= 20

        print (f'Бьет {self.name} у противника осталось здоровья {hp}')
        return self.health

warrior_1 = Warrior('Воин 1',100)
warrior_2 = Warrior('Воин 2',100)

while warrior_1.health > 0 and warrior_2.health > 0:
    who_hits = random.randint(1, 2)
    if who_hits == 1:
        warrior_1.print_info(warrior_2.name,warrior_2.health)
    else:
        warrior_2.print_info(warrior_1.name,warrior_1.health)
else:
    if warrior_1.health > warrior_2.health:
        print (f'\nПобедил {warrior_1.name}, у него осталось {warrior_1.health} едениц здоровья')
    else:
        print(f'\nПобедил {warrior_2.name}, у него осталось {warrior_2.health} едениц здоровья')

