list_number = [num for num in range(10)]
print (list_number)
new_list_number = [(num,num +1) for num in range(0,10,2)] # работает не совсеми списками
new_list_number2 = [(value,list_number[index+1])for index, value in enumerate(list_number) if index % 2 == 0]
print (new_list_number)
print (new_list_number2)

