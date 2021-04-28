class Parents:

    def __init__(self, name, ages, list_children):
        self.name = name
        self.ages = ages
        self.list_children = list_children

    def print_info(self):
        print(f'Мое имя {self.name}, мне {self.ages} лет')
        print('Мои дети: ', end='')
        for i_children in self.list_children:
            print(i_children, end=' ')

    def calm_the_child(self, children):
        if children.calmness == True:  # TODO, можно просто "if children.calmness"
            print('Ребенок успокоился')
            return children.calmness == False

    def feed_the_baby(self, children):
        if children.hunger() == True:  # TODO, можно просто "if children.hunger()"
            print('Ребенок покормлен')
            return children.hunger == False


class Children:

    def __init__(self, name, ages, calmness, hunger):
        self.name = name
        self.ages = ages
        self.calmness = calmness
        self.hunger = hunger

    def calmness(self):
        if self.calmness == 'Да':
            return True
        return False

    def hunger(self):
        if self.hunger == 'Да':  # TODO, можно сразу так "return self.hunger == 'Да'"
            return True
        return False


perens = Parents('Коля', 31, ['Ваня', 'Лиза'])
perens2 = Parents('Маша', 27, ['Ваня', 'Лиза'])
children1 = Children('Ваня', 1, 'Да', 'Нет')
children2 = Children('Лиза', 2, 'Нет', 'Нет')
children1.hunger()
