lst_poteto = []


class Potesto:
    states_ripe = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    # , пожалуйста, обратите внимание, states без self это элемент доступный всем объектам класса.
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
        print(f'Картошка {self.index} сейчас {self.states_ripe[self.states]}')


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
        self.ridge = PotetoGarden(ridge)
        # , таким образом в грядке будет только 1 картошка.
        #  Предлагаю передавать в грядку сразу грядку картошек.
        #  Грядка - это список объектов Potesto. И соответствует классу PotetoGarden.

        # , одну картошку в грядку мы передавали бы так Potesto(index)
        #  По идее, необходимо создать аргумент с self и присвоить ему по такому же принципу грядку,
        #  но вместо index указать числовое значение. Ведь оно отвечает за количество картошек
        # Грядку с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой)????

    def look_after(self):
        #  в этом методе необходимо обращаться к "своей" грядке.

        # TODO, пожалуйста, поправьте название переменной "i", это ведь "картошка"? =)
        for i in self.ridge.potetoes:
            i.states += 2
            # TODO, картошку стоить собирать, только если созрела. Верно?
            #  В harvest предлагаю передавать только картошку. Внутри метода harvest мы можем обратиться
            #  к любому аргументу переменной "i"
            self.harvest(i.index, i.states_ripe[i.states])
        print(f'{self.name} ухаживает за грядкой, картошка растет быстрее')

    def harvest(self, num_poteyto, states):
        lst_poteto.append((num_poteyto, states))
        # TODO, если картошку собрали, то стоит убрать её с грядки.
        print(lst_poteto)
