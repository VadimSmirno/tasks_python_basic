import random

number = int(input('Сколько чисел будет? '))
number_list = [random.randint(0, 5) for _ in range(number)]
count_0 = number_list.count(0)
new_list = [index for index in reversed((sorted(number_list)))]
print('Сжатый список: ', new_list)
result = [i_new_list for i_new_list in new_list if i_new_list != 0]
print('Список без "0" : ', result)

# зачёт!
