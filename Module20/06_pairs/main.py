import random

list_number = [random.randint(0, 30) for _ in range(10)]
print('Оригинальный список: ', list_number)
new_list_number = [(list_number[num], list_number[num + 1]) for num in range(0, len(list_number) - 1, 2)]

new_list_number2 = [(value, list_number[index + 1]) for index, value in enumerate(list_number) if index % 2 == 0]
print('Новый список: ', new_list_number)
print('Новый список: ', new_list_number2)

# зачёт!
