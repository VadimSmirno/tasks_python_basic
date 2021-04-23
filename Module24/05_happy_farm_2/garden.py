class Potesto:
    states = {0: 'Отсутствует', 1: 'Росток',2:'Зеленая',3:'Зрелая'}

    def __init__(self,index):
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
        print (f'Картошка {self.index} сейчас {self.states}')



class PotetoGarden:

    def __init__(self, count):
        self.potetoes = [Potesto(index) for index in range(1,count+1)]

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
            print ('Вся картошка созрела, можно собирать\n')