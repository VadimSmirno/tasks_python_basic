text = input('Сообщение: ')

symbol = ''
list_symbol = []
for i_text in text:
    if i_text.isalpha() == True:
        symbol += i_text
    if i_text.isalpha() == False:
        list_symbol.append(symbol)
        list_symbol.append(i_text)
        symbol = ''


for i_list_symbol in list_symbol:
    print (i_list_symbol[::-1], end = '')