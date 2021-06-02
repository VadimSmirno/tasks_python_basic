import time
import datetime
import functools
from typing import Callable

def timer(func:Callable,name_class:str)->Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        finish = round((end - start),3)
        print(f'Завершение {name_class}.{func.__name__}  Время работы {finish}s')
        return result
    return wrapped_func

def log_methods(data:str)->Callable:
    def createtime(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr (cls,i_method_name)
                decorator_method = timer(cur_method,cls.__name__)
                setattr(cls,i_method_name,decorator_method)
                print(f'Запускается {cls.__name__}.{i_method_name}',end=' ')
                print('Дата и время запуска: ',
                      datetime.datetime.now().strftime(''.join(['%' + i if i.isalpha() else i for i in data])))
        return cls
    return createtime

@log_methods("b d Y - H:M:S")
class A:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
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
