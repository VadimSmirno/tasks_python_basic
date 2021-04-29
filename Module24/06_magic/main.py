class Water:

    name = 'Вода'

    def __add__(self, other):
        return Air()


class Air:

    name = 'Воздух'

class Fire:

    name = 'Огонь'


class Earth:

    name = 'Земля'