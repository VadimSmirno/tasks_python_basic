class Parents:

    def __init__(self,name,ages,list_children):
        self.name = name
        self.ages = ages
        self.list_children = list_children

    def print_info(self):
        print (f'Мое имя {self.name}, мне {self.ages} лет')
        print('Мои дети: ',end='')
        for i_children in self.list_children:
            print(i_children, end=' ')

    def calm_the_child(self):
        print('Ребенок успокоился')

    def feed_the_baby(self):
        print ('Ребенок покормлен')


class Children:

    def __init__(self,name,ages,calmness,hunger):
        self.name = name
        self.ages = ages
        self.calmness = calmness
        self.hunger = hunger


    def calmness(self):
        if self.calmness == 'Нет':
            perens.calm_the_child()



    def  hunger(self):
        if self.hunger == 'Нет':
            perens.feed_the_baby()


perens = Parents('Коля', 31, ['Ваня','Лиза'])
perens2 = Parents('Маша', 27, ['Ваня','Лиза'])
children1 = Children('Ваня', 1, 'Да','Нет')
children2 = Children('Лиза', 2, 'Нет','Нет')
children2.hunger()