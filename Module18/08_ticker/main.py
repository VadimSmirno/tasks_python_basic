
first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')


for step in range (1, len(first_line) +1):
    first_line = first_line[-1:] + first_line[:-1]
    if first_line == second_line:
        print (f'Первая строка получается из второй со сдвигом {step}')
        break
    if step == len(first_line ) :
        print ('Первую строку нельзя получить из второй с помощью циклического сдвига.')
