number = int(input('Введите количество заказов: '))
dict_order = {}
for i_order in range (1, number + 1):
    print(f'{i_order} заказ: ', end='')
    order = input().lower().split()

    # TODO, для сокращения количества вычислений, предлагаю создать переменные
    #  order[0] ... и далее в цикле работать с ними =)


    # TODO, по идее, нам потребуется 3 условия
    #  если покупателя ещё нет,
    #  если есть, но в заказе нет такой пиццы.
    #  если есть и в заказе уже есть пица.
    if order[0] in dict_order:
        dict_order[order[0]].update({order[1] : int(order[2])})



    else:
        dict_order[order[0]] =  {
                    order[1] : int(order[2])
                }

    # if order[1] in dict_order[order[0]] and len(dict_order[order[0]]) > 1:

print (dict_order)
