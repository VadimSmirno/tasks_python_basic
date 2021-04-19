def treatment(info):
    try:
        if len(info) < 3:
            raise ValueError
        for i_elem in info[0]:
            if not i_elem.isalpha():
                raise NameError
        if  '@' not in info[1] and '.' not in info[1]:
             raise SyntaxError
        if int(info[2]) < 10 or int(info[2]) > 99:
            raise ValueError

    except ValueError:
        return 1
    except NameError:
        return 1
    except SyntaxError:
        return 1
    else:
        return 0


file = open('registrations.txt', 'r', encoding='UTF-8')
for i_sym in file:
    id_people = i_sym.split()
    if treatment(id_people) == 0:
        reg_good = open('registrations_good.log', 'a')
        reg_good.write(f'{id_people}\n')
        reg_good.close()
    else:
        reg_bag = open('registrations_bad.log','a')
        reg_bag.write(f'{id_people}\n')
        reg_bag.close()

file.close()
