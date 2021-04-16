import  os
def file_write():
    with open(file_name, 'w') as file_object:
        file_object.write(text)


text = input ('Введите строку: ')
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
way = input('')
file_name = input((f'Введите имя файла: \n'))

while True:
    abs_path = os.path.abspath(file_name)
    # print(abs_path)
    check_file = os.path.exists(abs_path)
    print(check_file)
    if check_file == True:
        break
    else:
        print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
        way = input('')

if check_file:
    ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
    if ans_q == 'да':

        file_write()
        print(f'Файл успешно перезаписан!')
    else:
        print(f'Data is not record')
else:
    file_write()
    print(f'Файл успешно сохранён!')





