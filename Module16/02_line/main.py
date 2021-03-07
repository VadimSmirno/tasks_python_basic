first_class = []
second_class = []
first_class.extend(list(range(160, 177, 2)))
second_class.extend(list(range(162, 181, 3)))
new_list = []
sort_list = []
new_list.extend(first_class)
new_list.extend(second_class)
print(first_class)
print(second_class)
# print (sorted(new_list)) первый способ сортировки


for i in range(len(new_list)):  # второй способ сортировки
    sort_list.append(min(new_list))
    new_list.remove(min(new_list))
print(sort_list)

# TODO, возможно сможем написать свою функцию для сортировки списков без помощи функций sorted и min. =)
