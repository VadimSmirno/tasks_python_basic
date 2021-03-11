number_friends = int(input('Введите количество друзей: '))
number_of_lists = int(input('Количество долговых расписок: '))

list_number_friends = []
for num in range(1, number_friends + 1):
    list_number_friends.append([num, 0])

for index in range(1, number_of_lists + 1):
    print(index, ' Расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how = int(input('Сколько? '))
    for index_friends in list_number_friends:
        if index_friends[0] == to_whom:
            index_friends[1] += how
        if index_friends[0] == from_whom:
            index_friends[1] -= how

print('\nБаланс друзей:')

for i_element in list_number_friends:
    print()
    for j_element in i_element:
        print(j_element, end='  ')

# зачёт!
