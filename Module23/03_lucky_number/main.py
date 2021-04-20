import random

summ_number = 0
count = 0
while summ_number < 777:
    number = int(input('Введите число: '))
    summ_number += number
    file = open('num.txt', 'a')
    file.write(f'{str(number)}\n')
    number = random.randint(1,13)
    if number == 13:
        raise Exception ('Ошибка, куда разогнался?')

file2 = open('num.txt','r')
print (file2.read())
file2.close()