import os
def find_fail (cur_path):
    total_file = 0
    size_file = 0
    subdirectory = 0
    for i_elem in os.listdir(cur_path):
        if os.path.isfile(i_elem):
            size_file+=os.path.getsize(i_elem)/1024
            total_file += 1
            return  total_file,size_file,subdirectory

        if os.path.isdir(i_elem):
            subdirectory+=1
            find_fail(i_elem)





total_faile = 0
path = os.path.abspath('D:\\')
print (find_fail(path))
# 1) Создаем путь (например диск D)
# 2)Создаем функцию в которую передаем наш путь
# 3) В цикле проходим по списку который состоит из наших папок
# 4) если встречаем файл, то узнаем его "вес" и передаем значение переменной и увеличиваем счетчик количества файлов
# 5)а если встречаем директорию. то вызываем рекурсию и увеличиваем счетчик директории
# 6) функция должна выводить кортеж (количество файлов, общий размер файлов, количество подкаталогов)
