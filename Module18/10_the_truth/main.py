def cipher(line,step):
    char_list = [(alphabet[(alphabet.index(symbol) - step ) % 26])
                 if symbol != ' ' else ' ' for symbol in line]
    new_char_list = ''
    for i_char in char_list:
        new_char_list += i_char
    return new_char_list




text = 'vujgvmcfb tj ufscfu ouib zvhm jdjufyqm'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = cipher(text,1).split()
list_text = []
for i in result:
    if len (i) % 2 == 0:
        x = len(i)//2
        list_text.append(i[-x:] + i [:-x])
    else:
        x = len(i) // 3
        list_text.append(i[-x:] + i[:-x])
print (list_text)
# пока только до этого догадался.