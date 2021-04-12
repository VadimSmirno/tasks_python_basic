summ = 0

faile_number = open('numbers.txt', 'r')
for i_sym in faile_number:
    for i_num in i_sym:
        if i_num != ' ' and i_num != '\n':
            summ += int(i_num)
answer = open('answer.txt', 'w')
answer.write(str(summ))
faile_number.close()
answer.close()
