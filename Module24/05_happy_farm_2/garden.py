lst_poteto = []


class Potesto:
    states_ripe = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    # TODO, возможно, аргумент index лишний =)
    def __init__(self, index):
        self.index = index
        self.states = 0

    def grow(self):
        if self.states < 3:
            self.states += 1
        self.print_stets()

    def is_ripe(self):
        if self.states >= 3:
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

    def look_after(self):

        for i_potayto in self.ridge.potetoes:
            i_potayto.states += 2

            if i_potayto.is_ripe():
                self.harvest(i_potayto)
        print(f'{self.name} ухаживает за грядкой, картошка растет быстрее')

    def harvest(self, num_poteyto):

        lst_poteto.append(num_poteyto)

        # , таким образом удаляем все картошки, если созрела одна.
        #  При помощи какого спискового метода можно удалить конкретный элемент списка?
        # TODO, в целом, идея интересная. Предлагаю попробовать удалять методом remove.
        #  В таком случае, аргумент index у картошки получится лишним
        self.ridge.potetoes.remove(num_poteyto)
        print(lst_poteto)
