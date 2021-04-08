def min_len(string, cortege):
    return min(len(string), len(cortege))


def my_zip(object_, element):
    # TODO, таким образом возвращаем список. Как вернуть генератор?
    #  Отличие в скобка верно? =)
    result = [(object_[i_sym], element[i_sym]) for i_sym in range(min_len(object_, element))]
    return result

string = 'qwertyui'
cortege = (10, 20, 30, 40, 52)

for i_sym in (my_zip(string, cortege)):
    print (i_sym)
