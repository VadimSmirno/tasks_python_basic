import os

directory = input('Введите директорию ')

def gen_files_path(directory:str):
    result = os.walk(directory)
    yield result


function_result = gen_files_path(directory)
for i_generator in function_result:
    for j_directory in i_generator:
        print(j_directory)

# TODO, код выглядит недописаным. Функция должна содержать рекурсию =)
#  К примеру, у нас есть папка.
#  C:\Users\...\python_basic\Module26\02_refactoring
#  Пользователь должен указать начальную директорию
#  К примеру
#  C:\Users\...\python_basic\
#  И название папки 02_refactoring.
#  Необходимо рекурсией идти по всем папкам от "C:\Users\...\python_basic\ " до конца... =)
#  Если встречаем файл или папку - выводим название, в папку заходим и так, пока не найдём в директории папку "02_refactoring".
#  Давайте попробуем.
