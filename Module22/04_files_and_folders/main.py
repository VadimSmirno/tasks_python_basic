import os

faile = input('Введите название папки: ')
path = os.path.abspath(os.path.join('..', '..', faile))

lst = os.listdir(path)
size_file = 0
count_file = 0
count_subdirectory = 0
for i_direct in lst:
    path2 = os.path.abspath(os.path.join(path, i_direct))
    lst2 = os.listdir(path2)
    count_subdirectory += 1
    for i_file in lst2:
        size_file += os.path.getsize(i_file)
        # TODO, предлагаю попробовать перед получением размера сформировать полный путь к файлу исходя из path2 и i_file.
        #  Таким образом должно получится =)
        count_file += 1

print(f'Размер каталога: {size_file / 1024}')
print(f'Количество подкатологов: {count_subdirectory}')
print(f'Количество файлов: {count_file}')
