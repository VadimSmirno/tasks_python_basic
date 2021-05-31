import time
import datetime
import functools


def log_methods(data, decorator):
    # TODO, стоит добавить @functools.wraps для класса
    def createtime(cls):
        # TODO, этот wraps должен быть для функции.
        #  Т.к. функции это теже самые методы, время которых необходимо подсчитать =)
        @functools.wraps(cls)
        def wrapped_func(*args, **kwargs):
            instanse = cls(*args, **kwargs)
            # TODO внутри этой оболочки, стоит только подсчитывать время работы метода.
            #  т.к. эта оболочка относится к createtime
            for i_method_name in dir(cls):
                if i_method_name.startswith('__') is False:
                    cur_method = getattr(cls, i_method_name)
                    decorator_method = decorator(cur_method)
                    setattr(cls, i_method_name, decorator_method)
                    print(f'Запускается "{cls.__name__}.{i_method_name}".', end=' ')
                    print('Дата и время запуска: ',
                          datetime.datetime.now().strftime(''.join(['%' + i if i.isalpha() else i for i in data])))
            return instanse

        return wrapped_func
    # TODO, а в этом месте, когда время уже посчитали, находимся в оболочке log_methods.
    #  В этом месте стоит запускать цикл по методам класса и применять к ним функцию createtime для подсчёта времени =)

    return createtime


def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время работы {end - start}')
        return result

    return wrapped_func


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorator_method = decorator(cur_method)
                setattr(cls, i_method_name, decorator_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S", timer)
# @for_all_methods(timer)
class A:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S", timer)
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
