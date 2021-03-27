number = int(input('Введите количество заказов: '))
dict_order = {}
for i_order in range (1, number + 1):
    print(f'{i_order} заказ: ', end='')
    order = input().lower().split()  # создаю список ['имя','Название пиццы','количество']
    name = order[0]
    pizza = order[1]
    num = int(order[2])

    if name not  in dict_order:
        dict_order.update( {
            name:{pizza:num}
        })
    elif pizza not in dict_order[name]:
        dict_order[name].update({
            pizza : num
        })
    else:
        dict_order[name][pizza] += num

print (dict_order)

for i_name,j_dict_pizza in sorted(dict_order.items()):
    print('\n',i_name, ':')
    for i_pizza,j_num in sorted(dict(j_dict_pizza).items()):
        print (i_pizza, ':', j_num)
