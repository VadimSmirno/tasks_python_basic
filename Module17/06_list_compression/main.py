import  random
number = int(input('Сколько чисел будет? '))
number_list = [ random.randint(0,5) for _ in range(number)]
count_0 = number_list.count(0)
new_list = [index for index in reversed((sorted(number_list)))]
print ('Сжатый список: ',new_list)
print ('Список без "0" : ', new_list[:-count_0])