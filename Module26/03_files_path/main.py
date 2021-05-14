import os

directory = input('Введите директорию ')

def gen_files_path(directory:str):
    result = os.walk(directory)
    yield result


function_result = gen_files_path(directory)
for i_generator in function_result:
    for j_directory in i_generator:
        print(j_directory)
