number = int(input('Введите количество заказов: '))
dict_order = {}
for i_order in range (1, number + 1):
    print(f'{i_order} заказ: ', end='')
    order = input().lower().split()

    if order[0] in dict_order:
        dict_order[order[0]].update({order[1] : int(order[2])})



    else:
        dict_order[order[0]] =  {
                    order[1] : int(order[2])
                }

    # if order[1] in dict_order[order[0]] and len(dict_order[order[0]]) > 1:

print (dict_order)
