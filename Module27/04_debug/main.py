import functools


def debug(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('\nВызывается функция {func} {args}{kwargs}'.format(
            func=func.__name__, args=args, kwargs=kwargs,
        ))
        value = func(*args, **kwargs)
        print(f'{func.__name__} вернула значение: {value}')
        return value

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))

# зачёт!
