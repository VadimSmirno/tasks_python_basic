import os


def file_write(file_name):
    with open(file_name, 'w') as file_object:
        file_object.write(text)


text = input('Введите строку: ')

while True:

    print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
    way = '\\'.join(input('').split())
    file_name1 = input((f'Введите имя файла: \n'))
    file_name = f'{file_name1}.txt'
    abs_path = os.path.abspath(os.path.join(os.path.sep, way, file_name))
    print(abs_path)
    check_file = os.path.exists(abs_path)
    print(check_file)
    if check_file:
        break

if check_file:
    ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
    if ans_q == 'да':
        file_write(abs_path)
        print(f'Файл успешно перезаписан!')
    else:
        print(f'Data is not record')
else:
    file_write(abs_path)
    print(f'Файл успешно сохранён!')

# зачёт!
