import os

directory = input('Введите директорию ')

def gen_files_path(directory):
    count_len = 0
    for i_name_faile in os.listdir(directory):
        if os.path.isdir(directory + '\\' + i_name_faile):
            gen_files_path(directory + '\\' + i_name_faile)
        elif os.path.isfile(directory+ '\\' +i_name_faile) and i_name_faile.endswith('.py'):
            print(directory+ '\\' + i_name_faile)
            with open(directory+ '\\' + i_name_faile, 'r') as fail:
                for i_string in fail.readlines():
                    if '#' not in i_string or i_string:
                        count_len += 1
            yield count_len
        else:
            gen_files_path(directory + '\\' + i_name_faile)



function_result = gen_files_path(directory)
for i in function_result:
    print (i)