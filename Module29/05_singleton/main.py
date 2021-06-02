import functools
from typing import Callable


def singleton(cls) -> Callable:
    instances = {}  # TODO, возможно, словарь получился лишний.

    @functools.wraps(cls)
    def getinstance():  # TODO, стоит передавать арги и кваги =)
        if cls not in instances:
            # TODO, стоит в этом месте обращаться к instances функции getinstance.
            instances[cls] = cls()  # TODO, создавать объект класса стоит с аргами и кваргами.
        return instances[cls]  # TODO, возвращаем instances функции getinstance

    # TODO, или instances функции getinstance приравниваем к None и возвращаем =)
    return getinstance


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
