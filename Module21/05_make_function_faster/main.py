def calculating_math_func(data,fact = {}):
    if data in fact:
        result = fact[data]
        return result
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        fact[data] = result
    result /= data ** 3
    result = result ** 10
    return result

# TODO, в целом правильно, только в словарь необходимо положить значение, которое получаем перед возвратом.
#  Суть в том, чтобы сократить количество вычислений в функции и не запускать функцию второй раз,
#  если значение уже было посчитано. Таким образом мы экономим время работы кода, в случае повторных вычислений.

print(calculating_math_func(8))
print(calculating_math_func(8))

