first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_list.extend(second_list)
print ('Количество цифр 5 при первом объединениии: ',first_list.count(5))
first_list.remove(5)
for index in first_list:
    if index == 5:
        first_list.remove(index)
first_list.extend(third_list)
print ('Количество цифр 3 при втором объединении: ',first_list.count (3))
print('Итоговый список: ', first_list)