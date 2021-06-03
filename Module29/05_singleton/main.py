import functools
from typing import Callable


def singleton(cls) -> Callable:
    @functools.wraps(cls)
    def getinstance(*args,**kwargs):
        # TODO, только было бы правильней присвоить к getinstance.instances
        #  результат создания объекта класса и вернуть его.
        cls(*args,**kwargs)
        return cls.instances
    cls.instances = None # TODO cls, тоже стоит заменить на функцию getinstance.
    return getinstance


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
