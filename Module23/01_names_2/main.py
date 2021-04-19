def errors (error):
    with open('errors.log', 'a') as file_errors:
        file_errors.write(f'{str(error)}\n')


summ_symbol = 0
count = 0
try:
    with open('people.txt','r',encoding='UTF-8') as file_people:
        for i_sym in file_people:
            count += 1
            line = len(i_sym)
            if i_sym.endswith('\n'):
                line -= 1
            if line < 3:
                try:
                    raise BaseException
                except BaseException:
                    print(f'Длина {count} строки меньше 3 символов')
                    errors(BaseException)
            summ_symbol += line

except FileNotFoundError:
    print ('Файл не найден')
    errors(FileNotFoundError)

finally:
    print('Сумма символов', summ_symbol)
