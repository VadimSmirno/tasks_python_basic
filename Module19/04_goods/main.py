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


# TODO Получилось идеально! =) Молодец!
for key, value in goods.items():
    print (key, '- ',end='')
    quantity = 0
    result = 0
    # TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
    #  "i" не отражает =)
    for i in store[value]:
        result += i['quantity'] * i['price']
        quantity += i['quantity']
    print (quantity, 'шт, стоимость ', end='')
    print (result, 'руб')




