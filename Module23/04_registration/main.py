def treatment(info):
    # TODO, предлагаю в этой функции проверять строку и вызывать исключения.
    #  ловить ошибки стоит только в основном цикле for нашей программы =)
    try:
        if len(info) < 3:
            raise ValueError
        # TODO, цикл получился лишний isalpha можно применить к строке.
        for i_elem in info[0]:
            if not i_elem.isalpha():
                raise NameError
        if '@' not in info[1] and '.' not in info[1]:
            raise SyntaxError
        if int(info[2]) < 10 or int(info[2]) > 99:
            raise ValueError

    except (ValueError, NameError, SyntaxError):
        return 1
    else:
        return 0


file = open('registrations.txt', 'r', encoding='UTF-8')
for i_sym in file:
    # TODO, предлагаю  делать split внутри функции treatment.
    #  Если элементов меньше 3, вызывать ошибку.
    id_people = i_sym.split()
    if treatment(id_people) == 0:
        reg_good = open('registrations_good.log', 'a')
        reg_good.write(f'{id_people}\n')
        reg_good.close()
    else:
        # TODO, записывать в этот файл предлагаю в блоках except =)
        reg_bag = open('registrations_bad.log', 'a')
        reg_bag.write(f'{id_people}\n')
        reg_bag.close()

file.close()
