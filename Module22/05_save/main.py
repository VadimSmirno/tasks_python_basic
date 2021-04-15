import  os

text = input ('Введите строку: ')
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
path = '\\'.join(input().split())
name_file = input ('Введите имя файла: ')
user_path = os.path.abspath(os.path.join(os.path.sep,path,name_file))


# TODO. 1. Необходимо добавить контроль ввода.
#  Если директории не существует, запрашиваем список папок снова.
#  2. Стоит проверять, существует итоговый файл или нет, если да, спрашиваем, стоит его перезаписать или нет.


if os.path.exists(user_path):
    file = open(user_path, 'w')
    file.write(text)
    file = open(user_path,'r')
    data = file.read()
    print ('Файл успешно сохранён!')
    print (f'Содержимое файла: {data}')
    file.close()
else:
    print ('Путь к файлу не найден')


