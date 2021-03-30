def new_tuple (cortege, element):

    if cortege.count(element) == 1:
        return tuple(list(cortege)[list(cortege).index(element):])
    elif cortege.count(element) >= 2:
        lst_index = [i_key for i_key, i_value in enumerate (list(cortege)) if i_value == element]
        return tuple(list(cortege)[lst_index[0]+1:lst_index[1]+1])
    else:
        return ()

elem = input('Введите символ: ')

print (new_tuple(('a','2','b','c','2','4','2','5'), elem))
