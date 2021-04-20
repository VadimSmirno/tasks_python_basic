def treatment(info):
    id_people = info.split()
    if len(id_people) < 3:
       raise ValueError

    if not id_people[0].isalpha():
        raise NameError

    if '@' not in id_people[1] and '.' not in id_people[1]:
        raise SyntaxError

    if int(id_people[2]) < 10 or int(id_people[2]) > 99:
        raise ValueError



file = open('registrations.txt', 'r', encoding='UTF-8')
for i_sym in file:

    try:
        treatment(i_sym)
        reg_good = open('registrations_good.log', 'a')
        reg_good.write(i_sym)
        reg_good.close()

    except Exception:
        reg_bag = open('registrations_bad.log', 'a')
        reg_bag.write(i_sym)
        reg_bag.close()

file.close()
