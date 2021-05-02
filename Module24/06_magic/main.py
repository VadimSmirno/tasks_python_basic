class Water:
    """"" Класс вода """""

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()  # пар
        elif isinstance(other, Earth):
            return Mud()  # грязь
        else:
            return None


class Air:
    """" Класс воздух """""
    def __init__(self):
        self.name = 'Воздух'
    # TODO, остальные классы тоже стоит поправить =)
    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()  # молния
        elif isinstance(other, Earth):
            return Dust()  # пыль
        else:
            return None


class Fire:
    """" Класс огонь """""
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    """" Класс земля """""

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name


class Storm:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name

    def answer(self):
        return 'Вода + Воздух'


class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name

    def answer(self):
        return 'Вода + Огонь'


class Mud:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name

    def answer(self):
        return 'Вода + Земля'


class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name

    def answer(self):
        return 'Воздух + Огонь'


class Dust:

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name

    def answer(self):
        return 'Воздух + Земля'


class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name

    def ansver(self):
        return 'Огонь + Земля'


print(Water() + Air())
