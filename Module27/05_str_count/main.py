import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        value = func(*args, **kwargs)
        wrapped_func.count += 1
        print(f'Функция {func.__name__} вызывалась {wrapped_func.count} раз')
        return value

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

# зачёт!
