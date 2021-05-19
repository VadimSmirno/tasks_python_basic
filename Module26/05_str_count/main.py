import os

directory = input('Введите директорию ')


def gen_files_path(directory:str):
    count_line = 0

    for i_name_faile in os.listdir(directory):
        path = os.path.join(directory, i_name_faile)
        if os.path.isfile(path) and i_name_faile.endswith('.py'):
            print(path)
            with open(path, 'r') as fail:
                for i_line in fail.readlines():
                    if '#' not in i_line and i_line:
                        count_line += 1
            yield count_line


function_result = gen_files_path(directory)
for i_number_lines in function_result:
    print(i_number_lines)
