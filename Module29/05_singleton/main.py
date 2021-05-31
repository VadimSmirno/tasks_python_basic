import functools
from typing import Callable


class Singleton:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.instance = None

    def __call__(self, *args, **kwargs) -> Callable:
        if self.instance == None:
            self.instance = self.func(*args, **kwargs)
        return self.instance


# TODO, пожалуйста, обратите внимание, декоратор должен работать не функцией, а классом.
#  Реализуйте декоратор singleton, который превращает класс в одноэлементный.
#  То есть при множественном инициализации объекта этого класса будет сохранён
#  только первый инстанс, а все остальные попытки создания будут возвращать первый экземпляр.

@Singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
