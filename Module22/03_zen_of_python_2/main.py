zen_python = open('zen.txt', 'r')
words = 0
count_str = 0
dct = {}
letters = 0
for i_sym in zen_python:
    count_str += 1
    words += len(i_sym.split())
    for i_letter in i_sym.lower():
        if i_letter.isalpha():
            letters += 1
            if i_letter not in dct:
                #  или можно создавать ключ как блоке else но со значение 1 =)  # я не понял, что можно сделать,
                #  текущий мой код не рационален?
                dct_letter = {
                    i_letter: 1
                }
                dct.update(dct_letter)
            else:
                dct[i_letter] += 1

min_word = min(dct.values())
for key, value in dct.items():
    if value == min_word:
        print(f'Буква "{key}" встречается в тексте меньше всего')
        break
print('Строк в файле: ', count_str)
print('Слов в файле: ', words)
print(f'Букв в тексте: {letters}')
zen_python.close()

# зачёт!
