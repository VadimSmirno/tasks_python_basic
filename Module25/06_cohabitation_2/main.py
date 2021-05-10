class Person:



    def __init__(self,name):
        self.name = name
        self.happiness = 100
        self.degree_of_satiety = 30
        self.degree_satiety()

    def  degree_satiety(self):
        if self.degree_of_satiety < 0:
            return False

    def  eat(self):
        """"
        Кушать, степень сытости увеличивается на 1,
        Еда в холодильнике дома уменьшается на 10 ед.
        """""

        if hause.food_in_the_fridge > 10:
            hause.food_in_the_fridge-=10
            self.degree_of_satiety += 1
            print(f'{self.name} поел уровень сытности {self.degree_of_satiety} '
                  f'еды в холодильник {hause.food_in_the_fridge}')
        else:
            print ('еда закончилась нужно идти в магазин')
            wife.buy_products()

class Husband(Person):

    def pley(self):
        """"
        Муж играет в видео игры дожа счастья растет на 20 ед
        """""
        self.degree_of_satiety -= 10
        self.happiness += 20
        print (f'{self.name} поиграл уровень сытности {self.degree_of_satiety}'
               f'уровень счастья {self.happiness}')

    def  work(self):
        """
        Муж работает, деньги увеличиваются на 150 ед
        """""
        self.degree_of_satiety -= 10
        hause.money += 150
        print(f'{self.name} заработал денег. Семейный бюджет {hause.money}')
        self.pley()


class Wife(Person):
    """
    Жена ест
    покупает продукты деньги уменьшаются на 10 ед, еда увеличивается на 10 ед
    покупает шубу деньги уменьшаются на 350 ед, счастье растет на 60 ед
    убирается дома грязь  минус 100 ед
    """""
    def buy_products(self):
        """"
        Купить еды для людей и для кота.
        если денег больше 20 ед
        """""
        self.degree_of_satiety -= 10
        if hause.money > 20:
            hause.money -= 20
            hause.food_in_the_fridge += 10
            hause.cat_food += 10
            print (f'{self.name} сходила в магазин. Еды в холодильнике {hause.food_in_the_fridge}'
                   f'Еды у кота {hause.cat_food}'
                   f'Денег осталось {hause.money}')
        else:
            print ('Нижно отправлять мужа на работу')
            husband.work()

    def  buy_a_fur_coat(self):
        self.degree_of_satiety -= 10
        if hause.money > 350:
            hause.money -= 350
            self.happiness += 60
            print(f'Накопили денег, купили шубу уровень счастья  {self.name} {self.happiness}'
                  f'Денег осталось {hause.money}')

    def cleaning(self):
        self.degree_of_satiety -= 10
        if hause.dirt_in_the_house >= 100:
            hause.dirt_in_the_house -= 100
            print ('Нужно прибраться в доме')


class  Hause:
    def __init__(self):
        self.money = 100
        self.food_in_the_fridge = 50
        self.cat_food = 30
        self.dirt_in_the_house = 0

class Cat(Person):
    def  eat(self):
        """"
        Кот ест максимум по 10 единиц еды, 
        степень сытости растёт на два пункта за один пункт еды.
        """""

        if hause.cat_food > 10:
            hause.cat_food-=10
            self.degree_of_satiety += 2
            print(f'{self.name} поел, уровень сытности {self.degree_of_satiety}'
                  f'Еды у кота {hause.cat_food}')
        else:
            print ('Еды у еота мало нужно в магазин')
            wife.buy_products()

    def slip(self):
        self.degree_of_satiety -= 10
        print('Кот спит, проголодался')


    def tear_wallpaper(self):
        self.degree_of_satiety -= 10
        hause.dirt_in_the_house += 5
        print(f'{self.name} порвал обои'
              f'грязи в доме {hause.dirt_in_the_house}')





hause = Hause()
wife = Wife('Катя')
husband = Husband('Ваня')
cat = Cat('Барсик')

count = 0
while count < 365:
    wife.eat()
    husband.eat()
    cat.eat()
    if wife.degree_satiety() or husband.degree_satiety() or cat.degree_satiety():
        print ('Год не прожили')
        break
    count += 1

