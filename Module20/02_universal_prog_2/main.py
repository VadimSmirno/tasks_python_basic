def is_prime (number):
    count = 0
    for i_num in range (1, number + 1):
        if number % i_num == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def list_object (obj_ect):
    return [i_valuse for i_key, i_valuse in enumerate(obj_ect) if is_prime(i_key)==True]