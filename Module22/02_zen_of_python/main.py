
lst = []
zen_python = open ('zen.txt','r')
for i_sym in zen_python:
    if '\n' in i_sym:
        lst.append(i_sym[:(len(i_sym)-1)])
    else:
        lst.append(i_sym)

for i_lst in (lst[::-1]):
    print (i_lst)
zen_python.close()

