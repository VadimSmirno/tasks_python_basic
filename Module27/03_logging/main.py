import functools
import datetime


def logging(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('\nВызывается функция {func}\t\n'
              'Позиционные аргументы : {args}\t\n'
              'Именовынные аргументы: {kwargs}\t\n'
              'Документация:{doc}'.format(
            func=func.__name__, args=args, kwargs=kwargs, doc=func.__doc__
        ))
        try:
            result = func(*args, *kwargs)
            return result
        except Exception as err:
            time_err = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='UTF-8') as fail:
                fail.write(f'Ошибка в функции {func.__name__} {err}, время возникновения ошибки {time_err}\n')

    return wrapped_func


@logging
def squares_num(number):
    """
    генерируется список из квадратов чисел 
    от 0 до number
    """""
    result = [num ** 2 for num in range(number)]
    return result


squares_num(number='')

# зачёт!
