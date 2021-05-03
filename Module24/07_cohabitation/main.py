import random


class People:

    def __init__(self, name):

        self.name = name
        self.degree_hunger = 50

    def add_hause(self, hause):
        """Присвоить дом человеку"""""
        self.hause = hause

    def act(self):

        # , цикл while стоит реализовать вне класса.
        #  Метод act должен отвечать только за 1 день жизни человека.

        cub = random.randint(1, 2)
        # , класс People ничего не знает про переменную people1 т.к. она создаётся вне класса.
        #  И не должен! =) Предлагаю обращаться к "своим" аргументам.
        if self.degree_hunger < 20:
            people1.eat()
        elif cub == 1:
            self.work()
        elif cub == 2:
            self.eat()
        else:
            self.pley()

        if self.degree_hunger < 0:
            print('Человек умер от голода')

    def eat(self):
        """"Кушать"""""
        # , стоит добавить проверку, если денег нет, то не едим
        if self.hause.refrigerator_food < 10:
            self.Go_to_the_store_for_food()
        if self.hause.money > 0 and self.degree_hunger < 15:
            self.degree_hunger += 1
            self.hause.refrigerator_food -= 10
            print('Поел уровень сытности ', self.degree_hunger)
            print(f'Еды осталось {self.hause.refrigerator_food}')
        else:
            self.work()

    def work(self):
        """""Работать"""""
        self.degree_hunger -= 1
        self.hause.money += 1

        print('Заработал денег', self.hause.money, 'уровень сытности', self.degree_hunger)

    def Go_to_the_store_for_food(self):
        """""В магазин за едой"""""

        if self.hause.money > 0:
            self.hause.money -= 1
            self.degree_hunger += 1
            print(f'Сходил в магазин за едой. Уровень еды {self.degree_hunger}')
            print(f'Денег осталось {self.hause.money}')

    def pley(self):
        """"Играть"""""
        self.degree_hunger -= 1
        print('Поиграл осталось еды', self.degree_hunger)


class Hause:

    def __init__(self):
        self.refrigerator_food = 50
        self.money = 0


people1 = People('Вася')
hause = Hause()
people1.add_hause(hause)
people1.act()

count = 0
while count < 365:
    people1.act()
    count += 1

# TODO в целом, всё хорошо.
#  "Реализуйте такую программу и создайте двух людей, живущих в одном доме.
#  Проверьте работу программы несколько раз. Надеемся, эти люди живы..."
