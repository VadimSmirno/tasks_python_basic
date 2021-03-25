def revision(thing, num):
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    quantity = store[(goods[thing])][num]['quantity']
    price = store[(goods[thing])][num]['price'] * store[(goods[thing])][num]['quantity']
    return [quantity, price]


print('Лампа -', revision('Лампа', 0)[0], 'шт', 'стоимость', revision('Лампа', 0)[1], 'руб')
print('Стол - ', revision('Стол', 0)[0] + revision('Стол', 1)[0], 'шт', 'стоимость', revision('Стол', 0)[1] +
      revision('Стол', 1)[1], 'руб')
print('Диван -', revision('Диван', 0)[0] + revision('Диван', 1)[0], 'шт', 'стоимость', revision('Диван', 0)[1] +
      revision('Диван', 1)[1], 'руб')
print('Стул -', revision('Стул', 0)[0] + revision('Стул', 1)[0] + revision('Стул', 2)[0], 'шт', 'стоимость',
      revision('Стул', 0)[1] +
      revision('Стул', 1)[1] + revision('Стул', 2)[1], 'руб')

# TODO, предлагаю упростить решение и решить без функции.
#  Всего за 2 цикла по словарям. =)
#  Количество строк должно стать на порядок меньше, как и вычислений значений по ключам словарей.