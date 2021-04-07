def min_len(string, cortege):
    return min(len(string), len(cortege))


def my_zip(object_, element):
    result = [(object_[i_sym], element[i_sym]) for i_sym in range(min_len(object_, element))]
    print(result)
# TODO функция my_zip должна вернуть итерируемый объект.
#  Вывод необходимо осуществить при помощи цикла по этому объекту =)

string = 'qwertyui'
cortege = (10, 20, 30, 40, 52)

my_zip(string, cortege)
