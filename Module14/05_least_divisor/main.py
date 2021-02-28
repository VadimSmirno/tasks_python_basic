def divider(number):
    for numeral in range(2, number + 1):
        if number % numeral == 0:
            print('Наименьший делитель ', numeral)
            break


number = int(input('Введите число '))
divider(number)

# зачёт!
