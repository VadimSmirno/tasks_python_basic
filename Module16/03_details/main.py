shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700]
]
count = 0
summ = 0
part_name = input('Название детали: ')

# TODO, для сокращения количества срезов, предлагаю в этом цикле идти сразу по списку без конструкции range + len.
for i_shop in range(len(shop)):
    if shop[i_shop][0] == part_name:
        count += 1
        summ += shop[i_shop][1]

print('Количество деталей: ', count)
print('Общая сумма: ', summ)
