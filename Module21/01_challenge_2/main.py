def number(num):
    if num >= 1:
        number(num - 1)
        print(num, end=' ')


num = int(input('Введите число '))
number(num)

# зачёт!

