

zen_python = open ('zen.txt','r')


lst = zen_python.readlines()
for i_sym in lst[::-1]:
    del_n = i_sym.rstrip('\n')
    print (del_n)
zen_python.close()

