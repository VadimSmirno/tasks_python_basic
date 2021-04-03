d_phonebook = {}
finish_dict = {}
while True:
    act = input('Добавить контакт или найти? ').lower()
    if act == 'добавить':
        name = input('\nИмя? ').lower()
        surname = input('Фамилия? ').lower()
        telephone = input('Номер телефона: ')
        if (name,surname) in d_phonebook:
            print ('\nЭтот человек уже есть в списке Ваших контактов.')
        d_phonebook = {
            (name,surname): telephone
        }
        finish_dict.update(d_phonebook)
        print('\n',finish_dict,'\n')
    if act == 'найти':
        look_surname = input('Человека с какой фамилией Вы хотите найти? ').lower()
        for i_person, phone in finish_dict.items():
            if look_surname in i_person:
                print(i_person[0], i_person[1],'-', phone)


