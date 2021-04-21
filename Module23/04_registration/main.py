def treatment(info):
    id_people = info.split()
    if len(id_people) < 3:
        raise ValueError ('НЕ присутствуют все три поля:')

    if not id_people[0].isalpha():
        raise NameError ('Поле имени содержит НЕ только буквы')

    if '@' not in id_people[1] and '.' not in id_people[1]:
        raise SyntaxError ('Поле «Имейл» НЕ содержит @ и .(точку)')

    if int(id_people[2]) < 10 or int(id_people[2]) > 99:
        raise ValueError ('Поле «Возраст» НЕ является числом от 10 до 99:')


file = open('registrations.txt', 'r', encoding='UTF-8')
for i_sym in file:

    try:
        treatment(i_sym)
        with open('registrations_good.log', 'a') as reg_good:
            reg_good.write(i_sym)

    except Exception as err:
        print ('{}    - Этот email отправляется в bag   {}'.format(i_sym.rstrip('\n'),err))

        with open('registrations_bad.log', 'a') as reg_bag:
            reg_bag.write('{} email не подходит по указанным параметрам  {}\n'.format(i_sym.rstrip('\n'),err))


file.close()
