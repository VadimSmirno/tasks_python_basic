def is_prime(number):
    count = 0
    for i_num in range(1, number + 1):
        if number % i_num == 0:
            count += 1
    return count


def list_object(obj_ect):
    return [i_valuse for i_key, i_valuse in enumerate(obj_ect) if is_prime(i_key) == 2]


text = 'О Дивный Новый мир!'
print(list_object(text))

# зачёт!
