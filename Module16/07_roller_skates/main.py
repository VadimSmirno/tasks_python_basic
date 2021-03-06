skate_size_list = []
foot_size_list = []
count = 0
number_skates = int(input('Количество коньков: '))

# TODO, пожалуйста, поправьте названия переменных i_ns и i_np.
#  Названия должны отражать суть содержания переменных.

for i_ns in range(1, number_skates + 1):
    print('размер ', i_ns, 'пары: ', end='')
    skate_size = int(input())
    skate_size_list.append(skate_size)

number_people = int(input('\nКоличество людей: '))
for i_np in range(1, number_people + 1):
    print('Размер ноги', i_np, 'человека: ', end='')
    foot_size = int(input())
    foot_size_list.append(foot_size)

# TODO, предлагаю упростить решение. Не использовать функцию min.
#  Можно идти по списку с размерами людей в цикле и проверять наличие размера в списке с размерами коньков.
#  Если есть, к счётчику +1 и удаляем 1 элемент из списка с размерами коньков.

for _ in range(number_skates):
    if min(foot_size_list) <= min(skate_size_list):
        count += 1
        foot_size_list.remove(min(foot_size_list))
        skate_size_list.remove((min(skate_size_list)))
    elif min(foot_size_list) > min(skate_size_list):
        skate_size_list.remove((min(skate_size_list)))

print('Наибольшее количество людей которые могут взять ролики:', count)
