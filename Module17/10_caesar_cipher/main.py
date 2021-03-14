def cipher (line,step):
    char_list = [(alphabet[(alphabet.index(symbol) + step) % 33])
                 if symbol != ' ' else ' ' for symbol in line]
    new_char_list = ''
    for i_char in char_list:
        new_char_list += i_char
    return  new_char_list


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input ('введите сообщение: ')
step = int(input('Введите сдвиг: '))

finish_text = cipher (text,step)
print('Зашифрованное сообщение: ', finish_text)