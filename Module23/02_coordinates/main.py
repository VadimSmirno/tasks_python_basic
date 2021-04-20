import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y



def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    file = open('coordinates.txt', 'r')

    for line in file:
        value_one,value_two = line.split()
        res1 = 0
        res2 =0

        try:
            res1 = f(int(value_one), int(value_two))
            res2 = f2(int(value_one), int(value_two))
        except Exception:
            print('Ошибка в функции')

        number = random.randint(0, 100)
        file_2 = open('result.txt', 'w')
        my_list = sorted([str(res1), str(res2), str(number)])
        file_2.write(' '.join(my_list))


except Exception:
     print ("Что-то пошло не так ")
finally:
    file = open('coordinates.txt', 'r')
    file_2 = open('result.txt', 'w')
    file.close()
    file_2.close()