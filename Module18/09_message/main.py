text = input('Сообщение: ')

symbol = ''
list_symbol = []
for i_text in text:
    if i_text.isalpha() == True:  # TODO, лучше if i_text.isalpha()
        symbol += i_text
    if i_text.isalpha() == False:  # TODO, лучше else =)
        list_symbol.append(symbol)
        list_symbol.append(i_text)
        symbol = ''


for i_list_symbol in list_symbol:
    print (i_list_symbol[::-1], end = '')

# TODO, пока что решение не оптимально =)
#  Сообщение: Это задание очень! простое
#  отЭ еинадаз ьнечо!