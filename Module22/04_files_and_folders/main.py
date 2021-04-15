import os
size_file = 0

faile = input('Введите название папки: ')
path = os.path.abspath(os.path.join('..','..',faile))

number_file = []
lst = os.listdir(path)
for i_direct in lst:
    path2 = os.path.abspath(os.path.join(path,i_direct))
    lst2 = os.listdir(path2)
    number_file.extend(lst2)

    for i_file in lst2:
         size_file += os.path.getsize(i_file)
print (f'Размер каталога: {size_file/1024}')
print (f'Количество подкатологов: {len(lst)}')
print (f'Количество файлов: {len(number_file)}')


