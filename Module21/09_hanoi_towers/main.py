def distribution_disks(number, kernel, kernel2):
    if number == 1:
        print(f'Переложить диск {1} со стержня номер {kernel} на стержень номер {kernel2}')
    else:
        distribution_disks(number - 1, kernel, 6 - kernel - kernel2)
        print(f'Переложить диск {number} со стержня номер {kernel} на стержень номер {kernel2}')
        distribution_disks(number - 1, 6 - kernel - kernel2, kernel2)


number_disks = int(input('Введите количество дисков: '))
distribution_disks(number_disks, 1, 3)