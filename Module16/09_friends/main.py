number_friends = int(input('Введите количество друзей: '))
number_of_lists = int(input('Количество долговых расписок: '))

list_number_friends = []
for num in range(1, number_friends + 1):
    list_number_friends.append([num,0])






for index in range(1, number_of_lists + 1):
    print (index, ' Расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how = int(input('Сколько? '))
    for index_friends in list_number_friends:
        if  index_friends [0] == to_whom:
            index_friends [1] -= how
        if index_friends [0] == from_whom:
            index_friends [1] += how



print ('\nБаланс друзей:')


for i_element in list_number_friends:
    print ()
    for j_element in i_element:
        print (j_element, end='  ')

# TODO, в целом, задание решено правильно.
#  Только если кому, то это "+", а от кого, это "-". Сейчас наоборот =)
# Введите количество друзей: 3
# Количество долговых расписок: 2
# 1  Расписка
# Кому: 1
# От кого: 3
# Сколько? 150
# 2  Расписка
# Кому: 1
# От кого: 2
# Сколько? 150
#
# Баланс друзей:
#
# 1  -300
# 2  150
# 3  150
# Process finished with exit code 0
