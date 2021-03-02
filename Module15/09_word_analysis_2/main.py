def comparison(word_list):
    count = 0
    for i_mn in range(len(word_list)):
        if word_list[i_mn] == word_list[-(i_mn + 1)]:
            count += 1
    if count == len((word_list)):
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')


word = input('Введите слово: ')
word_list = list(word)

comparison(word_list)

# зачёт!
