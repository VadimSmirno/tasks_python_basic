line = 'Найдите в ней самое длинное слово, выведите  это слово и его длину.'
list_line = line.split(' ')
print('Исходная строка: ', line)
max_length = ''
for index in list_line:
    if (len(index)) > len(max_length):  # (len(index)) лучше len(index)
        max_length = index
max_number_symbol = len(max_length)
print(f'самое длинное слово "{max_length}", оно состоит из {max_number_symbol} букв')

# зачёт!
