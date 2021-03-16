name_file = input('Название файла: ')
symbol = '@№$%^&*()'

for i_symbol in symbol:
    if name_file.startswith(i_symbol):
        print ('Ошибка: название начинается на один из специальных символов')
        break
    elif name_file.endswith('.txt') or  name_file.endswith('.docx'):
        print ('Файл назван верно.')
        break
    else:
        print ('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        break