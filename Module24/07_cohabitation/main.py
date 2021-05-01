import  random



class People:

    def __init__(self,name ):
        self.name = name
        self.degree_hunger = 50

    def eat(self):
        """"Кушать"""""
        self.degree_hunger += 1
        eat = Hause()
        eat.refrigerator_food -= 1
        print ('Поел уровень сытности ', self.degree_hunger)
        print (f'Еды осталось {eat.refrigerator_food}')

    def work(self):
        """""Работать"""""
        self.degree_hunger -= 1
        moneys = Hause()
        moneys.money += 1
        print('Заработал денег', moneys.money)




    def Go_to_the_store_for_food(self):
        """""В магазин за едой"""""
        moneys = Hause()
        moneys.money -= 1
        self.degree_hunger += 1
        print (f'Сходил в магазин за едой. Уровень еды {self.degree_hunger}')
        print(f'Денег осталось {moneys.money}')

    def pley(self):
        """"Играть"""""
        self.degree_hunger -= 1

class Hause:


    def __init__(self):
        self.refrigerator_food = 50
        self.money = 0

people1 = People('Вася')
count = 0
while count < 365:
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