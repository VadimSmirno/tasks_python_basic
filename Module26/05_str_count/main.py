import os

directory = input('Введите директорию ')

def gen_files_path(directory):
    count_line = 0
    for i_name_faile in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, i_name_faile)):
            gen_files_path(os.path.join(directory, i_name_faile))
        elif os.path.isfile(os.path.join(directory, i_name_faile)) and i_name_faile.endswith('.py'):
            print(os.path.join(directory, i_name_faile))
            with open(os.path.join(directory, i_name_faile), 'r') as fail:
                for i_line in fail.readlines():
                    if '#' not in i_line and i_line:
                        count_line += 1
            yield count_line
        else:
            gen_files_path(os.path.join(directory, i_name_faile))



function_result = gen_files_path(directory)
for i_number_lines in function_result:
    print (i_number_lines)