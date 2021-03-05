guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


ask = input ('Гость пришел или ушел? ')
while ask != 'Пора спать':
    name_guest = input('Имя гостя: ')
    if ask == 'пришел' and len(guests) < 6:
        guests.append(name_guest)
        print('Привет', name_guest)
    elif ask == 'ушел':
        if name_guest in guests:
            guests.remove(name_guest)
            print ('Пока', name_guest)
        else:
            print ('Человека с именем',name_guest,'нет в гостях')
    else:
        print('Прости,', name_guest,', но мест нет')
    print('Сейчас на вечеринке', len(guests), ' человек', guests)
    ask = input('Гость пришел или ушел? ')
