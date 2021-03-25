number = int(input('Введите количество пар слов:'))
dict_words = {}

for num in range(1,number+1):
    print (f'{num} пара: ', end='')
    words = input().lower().split(' - ')
    dict_words[words[0]] = words[1]
    dict_words[words[1]] = words[0]


while True:
    search_word = input ('Введите слово: ').lower()
    if search_word in dict_words:
        print ('Синоним', dict_words[search_word])
        break
    else:
        print('Такого слова в словаре нет.')