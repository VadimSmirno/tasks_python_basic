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


print(calculating_math_func(8))

