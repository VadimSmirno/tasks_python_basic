
word = input('Введите слово:')
word_list = list (word)
count = 0
new_word_list =[]
num = 0

for i_mn in range(len(word_list)):
    num += 1
    for curr in range(num, len(word_list)):
        if word_list[i_mn] == word_list[curr]:
            count += 1

print ('Количество уникальных букв', len(word_list)-count )


