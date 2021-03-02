start_list = [1,2,3,4,5]
shift = int(input('Сдвиг: '))
finish_list =  []

for i in range (1,shift+1):
    finish_list.append(start_list[len(start_list)-i])

for index in start_list:
    finish_list.append(index)


finish_list=finish_list[:-shift]
print ('Изначальный список', start_list)
print ('Сдвинутый список',finish_list)