import  random



class People:

    def __init__(self,name ):
        # , стоит добавить аргумент "дом" изначально равный None
        #  И метод, в котором будем присваивать дом человеку.
        self.name = name
        self.degree_hunger = 50
        self.hause = None


    # TODO, объект класса "дом" стоит создавать вне класса.
    #  И передавать в этот метод, как аргумент
    def add_hause(self):
        """Присвоить дом человеку"""""
        self.hause = Hause()


    def eat(self):
        """"Кушать"""""
        # , стоит добавить проверку, если денег нет, то не едим

        if self.hause.money > 0:
            self.degree_hunger += 1

            self.hause.refrigerator_food -= 1
            print ('Поел уровень сытности ', self.degree_hunger)
            print (f'Еды осталось {self.hause.refrigerator_food}')
        else:
            self.work()

    def work(self):
        """""Работать"""""
        self.degree_hunger -= 1
        moneys = Hause()
        moneys.money += 1
        print('Заработал денег', moneys.money)


    def Go_to_the_store_for_food(self):
        """""В магазин за едой"""""
        # TODO , стоит добавить проверку, если денег нет, то не идём в магазин

        self.hause.money -= 1
        self.degree_hunger += 1
        print (f'Сходил в магазин за едой. Уровень еды {self.degree_hunger}')
        print(f'Денег осталось {self.hause.money}')

    def pley(self):
        """"Играть"""""
        self.degree_hunger -= 1

class Hause:

    def __init__(self):
        self.refrigerator_food = 50
        self.money = 0

people1 = People('Вася')

# TODO, стоит создать "дом" и передать в метод add_hause
people1.add_hause()
count = 0
while count < 365:
    # TODO Стоит добавить метод "act" у человека и перенести в него логику жизни за 1 день.
    #  Таким образом, сократим количество кода вне класса и в текущем цикле будем запускать только 1 метод.
    cub = random.randint(1, 6)


    if people1.degree_hunger < 20:
        people1.eat()
    elif Hause().refrigerator_food < 50:
         people1.work()
    elif cub == 1:
        people1.work()
    elif cub == 2:
        people1.eat()
    else:
        people1.pley()
    count += 1
    if people1.degree_hunger < 0:
        print ('Человек умер от голода')
        break