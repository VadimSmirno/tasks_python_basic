
lst = []
zen_python = open ('zen.txt','r')
for i_sym in zen_python:
    # TODO, предлагаю попробовать убрать лишние пробелы в строке перед начало действий =)
    #  Кстати, чтобы получить из файла итерируемый объект, можно попробовать использовать метод readlines().
    if '\n' in i_sym:
        lst.append(i_sym[:(len(i_sym)-1)])
    else:
        lst.append(i_sym)

for i_lst in (lst[::-1]):
    print (i_lst)
zen_python.close()

