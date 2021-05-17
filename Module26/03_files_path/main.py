import os

directory = input('Введите директорию ')
name_faile = input('Какой файл ищем? ')


def gen_files_path(directory: str, name_faile: str):
    for i in os.listdir(directory):
        # TODO, стоит поправить название переменной "i".
        #  Первым делом проверим, если "i" это файл, то возвращаем его название
        yield (directory + '\\' + i)  # TODO, конкатенация в заданиях с директориями лишняя =)
        # TODO, если "i" директория, то проверяем её базовое название.
        #  Если совпадает, то выходим из рекурсии.
        #  Если нет, то запускаем цикл по вызову функции gen_files_path.
        if i == name_faile:
            yield ('Файл найден', directory + '\\' + i)
            return

        elif os.path.isdir(directory + '\\' + i):
            gen_files_path((directory + '\\' + i), name_faile)


function_result = gen_files_path(directory, name_faile)
for i in function_result:
    print(i)

# D:\python_basic
# 03_files_path
