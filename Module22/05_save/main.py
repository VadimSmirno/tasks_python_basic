import  os

text = input ('Введите строку: ')
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
way = input('')
file_name = input((f'Введите имя файла: \n'))
test_path = way.replace(" ", "/")
path = str('C:/' + test_path)
newpath = str(test_path+"/"+file_name)
print(newpath)
abs_path = os.path.abspath(file_name)
print(abs_path)
check_file = os.path.exists(abs_path)
print(check_file)
if check_file:
    ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
    if ans_q == 'да':
        with open(file_name, 'w') as file_object:
            file_object.write(text)
            print(f'Файл успешно перезаписан!')
    else:
        print(f'Data is not record')
else:
    with open(file_name, 'w') as file_object:
        file_object.write(text)
        print(f'Файл успешно сохранён!')





