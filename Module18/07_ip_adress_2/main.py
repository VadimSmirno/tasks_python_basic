ip_adres = input('Введите IP адрес: ').split('.')
good_adres = []
for index in ip_adres:
    if index.isdigit() == False:
        print(f'{index} - не целое число')
        break
    elif int(index) > 255:
        print(f'{index} превышает 255')
        break
    elif len(ip_adres) != 4:
        print('Адрес - это четыре числа, разделённые точками')
        break
    else:
        good_adres.append(index)

if len(good_adres) == 4:
    print('IP-адрес корректен')

# зачёт!
