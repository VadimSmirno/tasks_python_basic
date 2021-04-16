text = open('text.txt', 'r')
print('Содержимое файла text.txt: ')
print(text.read())
text = open('text.txt', 'r')
lst = text.readlines()
count = 0
total_dct = {}
for i_elem in lst:
    for i_sym in i_elem.lower():
        if i_sym.isalpha():
            count += 1
            if i_sym not in total_dct:
                # или "total_dct[i_sym] = 1"
                dct = {
                    i_sym: 1
                }
                total_dct.update(dct)
            else:
                total_dct[i_sym] += 1
total_lst = []
for key, value in total_dct.items():
    tpl = (key, round(value / count, 3))
    total_lst.append(tpl)

result = sorted(total_lst, key=lambda x: (-x[1], x[0]))
analysis = open('analysis.txt', 'a')
for i_elem in result:
    analysis.write(i_elem[0] + ' ')  # TODO, для записи в файл предлагаю использовать форматирование.
    analysis.write(str(i_elem[1]) + '\n')

analysis = open('analysis.txt', 'r')
print('Содержимое файла analysis.txt:\n' + analysis.read())
text.close()
analysis.close()

