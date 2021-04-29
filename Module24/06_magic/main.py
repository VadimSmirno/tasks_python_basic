class Water:
    """"" Класс вода """""

    def __str__(self):
        return 'Вада'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()  # пар
        elif isinstance(other, Earth):
            return Mud()  # грязь


class Air:
    """" Класс воздух """""

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()  # молния
        elif isinstance(other, Earth):
            return Dust()  # пыль
        # TODO, иначе, возвращаем None.


class Fire:
    """" Класс огонь """""

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    """" Класс земля """""

    def __str__(self):
        return 'Земля'


class Storm:

    # TODO, стоит так же добавить метод __str__

    def answer(self):
        return 'Вода + Воздух'


class Steam:
    def answer(self):
        return 'Вода + Огонь'


class Mud:
    def answer(self):
        return 'Вода + Земля'


class Lightning:
    def answer(self):
        return 'Воздух + Огонь'


class Dust:
    def answer(self):
        return 'Воздух + Земля'


class Lava:
    def ansver(self):
        return 'Огонь + Земля'
