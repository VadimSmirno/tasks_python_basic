number_of_sticks = int(input('Количество палок: '))
throw = int(input('Количество бросков: '))

list_sticks = []
for _ in range(number_of_sticks):
    list_sticks.append('|')
for index in range(1, throw + 1):
    print('Бросок ', index, '. Сбиты палки с номера ', end='')
    start_sticks = int(input())
    print('по номер ', end='')
    stop_sticks = int(input())
    list_sticks[start_sticks - 1:stop_sticks] = ['.'] * (stop_sticks - start_sticks + 1)

for i_list_sticks in list_sticks:
    print(i_list_sticks, end='')

# зачёт!
