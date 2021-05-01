class Potesto:
    states_ripe = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    # TODO, пожалуйста, обратите внимание, states без self это элемент доступный всем объектам класса.
    #  self.states это элемент только для текущего объекта класса.
    #  И к одному и второму элементу необходимо обращаться через self.states
    #  Предлагаю один из states переименовать.

    def __init__(self, index):
        self.index = index
        self.states = 0


    def grow(self):
        if self.states < 3:
            self.states += 1
        self.print_stets()

    def is_ripe(self):
        if self.states == 3:
            return True
        return False

    def print_stets(self):
        print(f'Картошка {self.index} сейчас {self.states}')


class PotetoGarden:

    def __init__(self, count):
        self.potetoes = [Potesto(index) for index in range(1, count + 1)]

    def grow_al(self):
        print('Картошка прорастает')
        for i_potato in self.potetoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potetoes:
            if not i_potato.is_ripe():
                print('картошка еще не созрела\n')
                break

        else:
            print('Вся картошка созрела, можно собирать\n')


class Garden:

    def __init__(self, name, ridge):
        self.name = name
        self.ridge = Potesto(ridge)
        # TODO, одну картошку в грядку мы передавали бы так Potesto(index)
        #  По идее, необходимо создать аргумент с self и присвоить ему по такому же принципу грядку,
        #  но вместо index указать числовое значение. Ведь оно отвечает за количество картошек
        # Грядку с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой)????

    def look_after(self):
        # TODO в этом методе необходимо обращаться к "своей" грядке.
        self.ridge
        if Potesto.is_ripe:
            print('Собираю картошку')

    def harvest(self):
        lst_poteto = []
        # Как собирать урожай?
