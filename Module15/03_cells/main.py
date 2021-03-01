cell = int (input ('Количество клеток: '))
list_efficiency_cell = []
for num in range (1,cell+1):
    print ('эффективность ', num, ' клетки: ', end = '')
    efficiency_cell = int (input ())
    if num > efficiency_cell:
      list_efficiency_cell.append(efficiency_cell)

print ('Неподходящие значения: ', end = '')
for index in (list_efficiency_cell):
    print ( index, end = ' ')