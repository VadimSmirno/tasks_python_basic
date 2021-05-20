import functools
import datetime


def logging(func):
    @functools.wraps(func)
    def wrapped_func(*args,**kwargs):
        print ('\nВызывается функция {func}\t\n'
               'Позиционные аргументы : {args}\t\n'
               'Именовынные аргументы: {kwargs}\t\n'
            'Документация:{doc}'.format(
            func=func.__name__, args = args, kwargs = kwargs,doc = func.__doc__
        ))
        try:
            result = func(*args,*kwargs)
        except Exception("Упс") as err:
            time_err = datetime.time
            with open('function_errors.log', 'a', encoding='UTF-8') as fail:
                fail.write(f'Ошибка в функции {func} {err}, время возникновения ошибки {time_err}')

        print ('Функция успешно завершила работу')
        return result
    return wrapped_func

@logging
def squares_num(number):
    """
    генерируется список из квадратов чисел 
    от 0 до number
    """""
    result = [num**2 for num in range (number)]
    return result

squares_num(5)