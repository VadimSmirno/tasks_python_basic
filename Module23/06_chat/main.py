name = input ('Введите имя пользователя: ')
while True:
    print ('Посмотреть текущий текст чата - 1 , Отправить сообщение -2')
    result = input('Введите 1 или 2: ')
    if result == '1':
        try:
            with open ('chat.txt', 'r') as file:
                massages = file.readlines()
                print (''.join(massages))
        except FileNotFoundError:
            print ('Пока ничего нет\n')
    elif result == '2':
        new_massages = input('Введите сообщение: ')
        with  open('chat.txt', 'a') as file:
            file.write(f'{name} : {new_massages}')
