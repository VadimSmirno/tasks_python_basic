import functools
from typing import Callable


def singleton(cls) -> Callable:
    @functools.wraps(cls)
    def getinstance(*args,**kwargs):
        getinstance.instances = cls(*args,**kwargs)
        return getinstance.instances
    getinstance.instances = None
    return getinstance


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
