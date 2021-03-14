text = input('Введите текст: ')
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowels_text = [index for index in text if index in vowels]
print('Список гласных букв: ', vowels_text, '\nДлина списка: ', len(vowels_text))

# зачёт!
# зачёт!
