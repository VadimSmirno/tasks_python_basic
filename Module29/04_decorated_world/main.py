from typing import Callable, Any

def decorator_with_args_for_any_decorator(decorated_decorator:Callable)->Callable:
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorated_decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker



@decorator_with_args_for_any_decorator
def decorated_decorator(func:Any, *args, **kwargs)->Callable:
    def wrapped_func(function_arg1, function_arg2):
        print(f'Переданные арги и кварги в декоратор:{args}{kwargs}')
        value = func(function_arg1, function_arg2)
        return value
    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)