n = int(input('Введите число: '))
def summ_numeral (n):
    summ = 0
    while n > 0:
        summ += n%10
        n //= 10
    print ('Сумма цифр:', summ)
    return summ
def count_numeral (n):
    count = 0
    while n > 0:
        n//= 10
        count +=1
    print ('Количество цифр:', count)
    return count

print ('Разность суммы  и количества цифр:', summ_numeral(n) - count_numeral(n))


