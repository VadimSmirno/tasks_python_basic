import time
import datetime
import functools

def log_methods(data):
    def createtime(cls):
        @functools.wraps(cls)
        def wrapped_func(*args,**kwargs):
            instanse = cls(*args,**kwargs)
            for i_method_name in dir(cls):
                if i_method_name.startswith('__') is False:

                    print(f'Запускается {cls.__name__} {i_method_name}',end=' ')
                    print ('Дата и время запуска',
                           datetime.datetime.now().strftime(''.join(['%' + i if i.isalpha() else i for i in data])))
            return instanse
        return wrapped_func
    return createtime

def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args,**kwargs):
        start=time.time()
        result =func(*args,**kwargs)
        end = time.time()
        print(f'Время работы {end - start}')
        return result
    return wrapped_func


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls,i_method_name)
                decorator_method = decorator(cur_method)
                setattr(cls,i_method_name,decorator_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
@for_all_methods(timer)
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
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
