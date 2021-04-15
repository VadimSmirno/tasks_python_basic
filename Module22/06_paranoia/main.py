def cipher(line, step):
    char_list = [(alphabet[(alphabet.index(symbol) + step) % 26])
                 if symbol != ' ' else ' ' for symbol in line]
    new_char_list = ''
    for i_char in char_list:
        new_char_list += i_char
    return new_char_list


text = open('text.txt', 'r')
print('Содержимое файла text.txt:')
print(text.read())
count = 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i_sum in text:
    result = cipher(i_sum.rstrip('\n').lower(), count)
    count += 1
    cipher_text = open('cipher_text.txt', 'a')
    cipher_text.write(result + '\n')

print('Содержимое файла cipher_text.txt:')
cipher_text = open('cipher_text.txt', 'r')
print(cipher_text.read())
text.close()
cipher_text.close()

# зачёт!
