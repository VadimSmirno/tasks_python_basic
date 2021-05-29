from typing import Callable
import functools


def check_permission(user_name: str) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            try:
                # TODO, стоит проверять наличие пользователя в списке user_permissions =)
                if user_name != 'admin'.lower():
                    raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
                result = func(*args, **kwargs)
                return result
            except PermissionError as err:
                print('PermissionError:', err)

        return wrapped_func

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
