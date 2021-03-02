
word = input('Введите слово:')
word_list = list (word)
count = 0
new_word_list =[]

for index in word_list:
    if index not in new_word_list:
        new_word_list.append(index)
        count+=1


print ('Количество уникальных букв', count )
print ('Уникальные буквы', new_word_list)