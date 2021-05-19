import os

directory = input('Введите директорию ')
name_faile = input('Какой файл ищем? ')


def gen_files_path(directory: str, name_faile: str):
    count = 0
    for i_name_faile in os.listdir(directory):
        if os.path.isfile(i_name_faile):
            yield i_name_faile
        elif os.path.isdir(i_name_faile):
            if os.path.basename(i_name_faile) == name_faile:
                return os.path.join(directory, i_name_faile)

        while count < len(os.listdir(directory)):
            count += 1
            gen_files_path(os.path.join(directory, i_name_faile), name_faile)
            yield os.path.join(directory, i_name_faile)


function_result = gen_files_path(directory, name_faile)
for i in function_result:
    print(i)


# D:\python_basic
# 03_files_path


def direc(directory, name_faile):
    for root, dirs, file in os.walk(directory):
        yield root
        if os.path.basename(root) == name_faile:
            print('Нашел')
            return


result = direc(directory, name_faile)
for i in result:
    print(i)

# зачёт!
