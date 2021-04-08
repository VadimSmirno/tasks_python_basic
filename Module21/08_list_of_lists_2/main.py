def lst (element):
    if element == []:
        return (element)
    if isinstance(element[0],list):
        return lst(element[0] + lst(element[1:]))
    return (element[:1] + lst((element[1:])))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


print ('Ответ ', lst(nice_list))