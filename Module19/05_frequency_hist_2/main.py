def list_new_hist(new_hist, num):
    new_hist = [key for key, values in hist.items() if values == num]
    return new_hist


def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input('Введите текст: ').lower()
hist = histogram(text)
print('Оригинальный словарь частот:\n')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])
values = set(hist.values())
print('\nИнвертированный словарь частот :\n')
for i_values in values:
    print(i_values, ':', list_new_hist(hist, i_values))

# зачёт!
