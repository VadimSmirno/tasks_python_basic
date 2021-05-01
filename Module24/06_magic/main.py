class Water:
    """"" Класс вода """""


    # TODO, в целом, решение верное!
    #  Предлагаю создать метод init и определить в нём имя класса "Вода".
    #  А в методе __str__ возвращать имя класса. =)

    def __str__(self):
        return 'Вада'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()  # пар
        elif isinstance(other, Earth):
            return Mud()  # грязь
        else:
            return  None


class Air:
    """" Класс воздух """""

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()  # молния
        elif isinstance(other, Earth):
            return Dust()  # пыль
        else:
            return None



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

    def __str__(self):
        return 'Шторм'

    def answer(self):
        return 'Вода + Воздух'


class Steam:

    def __str__(self):
        return 'Пар'

    def answer(self):
        return 'Вода + Огонь'


class Mud:

    def __str__(self):
        return 'Грязь'

    def answer(self):
        return 'Вода + Земля'



class Lightning:

    def __str__(self):
        return 'Молния'

    def answer(self):
        return 'Воздух + Огонь'


class Dust:

    def __str__(self):
        return 'Пыль'

    def answer(self):
        return 'Воздух + Земля'


class Lava:

    def __str__(self):
        return 'Лава'

    def ansver(self):
        return 'Огонь + Земля'

