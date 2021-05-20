import functools
from typing import Callable

def how_are_you(func:Callable)->Callable:

    """"
    декорратор печетает дополнительный текст
    перед вызовом основной фкункции
    """""
    @functools.wraps(func)
    def wrapped_func()->None:
        print ('Как дела?\nХорошо.\nА у меня не очень!\nЛадно, держи свою функцию.')
        func()
        return
    return wrapped_func

@how_are_you
def test()-> None:
    print('<Тут что-то происходит...>')

test()