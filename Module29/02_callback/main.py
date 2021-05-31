import functools
from  typing import Callable

app = {}
def callback(sumbol)->Callable:
    def decorator(func):
        app[sumbol] = func
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapped_func
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
