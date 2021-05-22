import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        value = func(*args, **kwargs)
        wrapped_func.count += 1
        # TODO, пожалуйста, добавьте вывод количества в декораторе.
        return value, wrapped_func.count  # TODO wrapped_func.count возвращать не нужно =)

    wrapped_func.count = 0
    return wrapped_func


@counter
def square_num(number: int) -> list:
    square = [num ** 2 for num in range(number + 1)]
    return square


@counter
def cubs_num(number: int) -> list:
    cubs = [num ** 3 for num in range(number + 1)]
    return cubs


square_num(6)
square_num(4)
square_num(3)
cubs_num(4)
cubs_num(6)
cubs_num(4)
print(f'Функция {cubs_num.__name__} вызывалась {cubs_num(3)[1]} раз')
print(f'Функция {square_num.__name__} вызывалась {square_num(6)[1]} раз')
