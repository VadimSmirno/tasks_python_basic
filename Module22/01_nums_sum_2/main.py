summ = 0

faile_number = open('numbers.txt', 'r')
for i_sym in faile_number:
    if i_sym.strip().isdigit():
        summ += int(i_sym)

answer = open('answer.txt', 'w')
answer.write(str(summ))
faile_number.close()
answer.close()

# зачёт!
