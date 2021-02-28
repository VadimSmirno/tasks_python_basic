first_year = int(input('Введите первый год '))
second_year = int(input('Введите второй год '))

for year in range(first_year, second_year):
    a = year % 10
    b = year % 100 // 10
    c = year // 100 % 10
    d = year // 1000
    if a == b == c or b == c == d or a == d == b:
        print(year)

# зачёт!
