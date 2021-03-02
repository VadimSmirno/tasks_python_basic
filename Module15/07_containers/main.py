number_box = int(input('Количество контейнеров: '))
list_weight_box = []
new_list_weight_box = []

while number_box != 0:
    weight_box = int(input('Введите вес контейнера: '))
    if weight_box < 200:
        list_weight_box.append(weight_box)
    else:
        print('Контейнер слишком тяжелый')
        number_box += 1
    number_box -= 1
print(list_weight_box)

new_weight_box = int(input('\n\nВведите вес нового контейнера: '))

for index in list_weight_box:
    if index >= new_weight_box:
        new_list_weight_box.append(index)

print('Номер куда встанет новы контейнер', len(new_list_weight_box) + 1)

# зачёт!
