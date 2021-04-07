def fibonacci (num):
    if num in (1,2):
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

num_pos = int(input('Введите позицию в ряде Фибоначчи: '))
print (fibonacci(num_pos))