class Person:

    def __init__(self, name):
        self.name = name
        self.happiness = 100
        self.degree_of_satiety = 30
        # self.hause = None


    def add_hause(self, hause):
        """Присвоить дом человеку"""""
        self.hause = hause
        return self.hause

    def degree_satiety(self):
        if self.degree_of_satiety < 0:
            return False

    def eat(self):
        """"
        Кушать, степень сытости увеличивается на 1,
        Еда в холодильнике дома уменьшается на 10 ед.
        """""

        if  self.hause.food_in_the_fridge > 10:
            self.hause.food_in_the_fridge -= 10
            self.degree_of_satiety += 1
            print(f'{self.name} поел уровень сытности {self.degree_of_satiety} '
                  f'еды в холодильник {self.hause.food_in_the_fridge}')
        else:
            print('Еда закончилась нужно идти в магазин')
            # TODO, в этом методе еду не покупаем, только едим если можем =)



class Husband(Person):

    def act(self):
        if self.degree_of_satiety < 0 or self.happiness < 0:
            return True
        if self.degree_of_satiety < 5 and self.hause.food_in_the_fridge > 0:
            self.eat()
        elif self.hause.food_in_the_fridge < 5:
            self.work()
        elif self.hause.dirt_in_the_house >=90:
            self.happiness -=10
        else:
            self.pley()


    def pley(self):
        """"
        Муж играет в видео игры дожа счастья растет на 20 ед
        """""
        self.degree_of_satiety -= 10
        self.happiness += 20
        print(f'{self.name} поиграл уровень сытности {self.degree_of_satiety} '
              f'Уровень счастья {self.happiness}')

    def work(self):
        """
        Муж работает, деньги увеличиваются на 150 ед
        """""
        self.degree_of_satiety -= 10
        self.hause.money += 150
        print(f'{self.name} заработал денег. Семейный бюджет {self.hause.money}')
        self.pley()


class Wife(Person):
    """
    Жена ест
    покупает продукты деньги уменьшаются на 10 ед, еда увеличивается на 10 ед
    покупает шубу деньги уменьшаются на 350 ед, счастье растет на 60 ед
    убирается дома грязь  минус 100 ед
    
    """""
    def act(self):
        if self.degree_of_satiety < 0 or self.happiness < 0:
            return True
        if self.hause.food_in_the_fridge or self.hause.cat_food < 5:
            self.buy_products()
        if self.hause.money >=350:
            self.buy_a_fur_coat()
        if self.hause.dirt_in_the_house > 90:
            self.cleaning()
        if self.hause.dirt_in_the_house >=90:
            self.happiness -=10

    def buy_products(self):
        """"
        Купить еды для людей и для кота.
        """""
        self.degree_of_satiety -= 10

        self.hause.money -= 20
        self.hause.food_in_the_fridge += 10
        self.hause.cat_food += 10
        print(f'{self.name} сходила в магазин. Еды в холодильнике {self.hause.food_in_the_fridge} '
                f'Еды у кота {self.hause.cat_food} '
                f'Денег осталось {self.hause.money}')



    def buy_a_fur_coat(self):
        self.degree_of_satiety -= 10
        self.hause.money -= 350
        self.happiness += 60
        print(f'Накопили денег, купили шубу уровень счастья  {self.name} {self.happiness}'
                f'Денег осталось {self.hause.money}')

    def cleaning(self):
        self.degree_of_satiety -= 10
        if self.hause.dirt_in_the_house >= 100:
            self.hause.dirt_in_the_house -= 100
            print('Нужно прибраться в доме')


class Hause:
    def __init__(self):
        self.money = 100
        self.food_in_the_fridge = 50
        self.cat_food = 30
        self.dirt_in_the_house = 0



class Cat():

    def __init__(self,name):
        self.name = name
        self.degree_of_satiety_cat = 30

    def act_cat(self):
        if self.degree_of_satiety_cat < 0:
            return True
        elif self.hause.cat_food > 0 and self.degree_of_satiety_cat < 5:
            self.eat_cat()
        else:
            self.slip()
            self.tear_wallpaper()

    def add_hause_cat(self, hause):
        """Присвоить дом коту"""""
        self.hause = hause
        return self.hause

    def eat_cat(self):
        """"
        Кот ест максимум по 10 единиц еды, 
        степень сытости растёт на два пункта за один пункт еды.
        """""
        self.hause.cat_food -= 10
        self.degree_of_satiety_cat += 2


    def slip(self):
        self.degree_of_satiety_cat -= 10
        print('Кот спит, проголодался')

    def tear_wallpaper(self):
        self.degree_of_satiety_cat -= 10
        self.hause.dirt_in_the_house += 5
        print(f'{self.name} порвал обои '
              f'Грязи в доме {self.hause.dirt_in_the_house}')



wife = Wife('Катя')
wife.add_hause(hause=Hause())
husband = Husband('Ваня')
husband.add_hause(hause=Hause())
cat = Cat('Барсик')
cat.add_hause_cat(hause=Hause())


count = 0
while count < 365:

    wife.act()
    husband.act()
    cat.act_cat()
    count += 1
