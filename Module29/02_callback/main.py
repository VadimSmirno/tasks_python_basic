import functools


def callback(sumbol):  # TODO, по идее, возвращаем объект Callable =)
    def decorator(func):

        # TODO, предлагаю попробовать заполнять словарь в этой функции обёртке.

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            value = func(*args, **kwargs)
            app = {sumbol: value}  #  TODO, таким образом, каждый раз создаётся новый словарь. Предлагаю каждый раз добавлять только один ключ
            return value

        return wrapped_func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
