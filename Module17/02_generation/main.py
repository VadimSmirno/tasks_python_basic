number = int(input('Введите число: '))
list_number = [1 if index % 2 == 0 else index % 5 for index in range (number)]
print ('Результат: ', list_number)
