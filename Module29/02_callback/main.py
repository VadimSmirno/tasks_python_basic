import functools

def callback(sumbol):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args,**kwargs):
            value = func(*args,**kwargs)
            app = {sumbol:value}
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