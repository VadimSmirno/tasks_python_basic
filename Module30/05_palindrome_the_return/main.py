from collections import defaultdict

def can_be_poly(str):
    str_lower = str.lower()
    dct_count = defaultdict(int)
    for symbol in str_lower:
        if ord(symbol) >= 97 and ord(symbol) <=122:
            dct_count[symbol] += 1
    middle = ''
    for symbol in dct_count:
        if middle and dct_count[symbol] % 2 == 1:
            return False
        elif dct_count[symbol] % 2 == 1:
            middle = symbol
    return  True

print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

# TODO, перелагаю попробовать решить задание в одну сроку =)
#  Стоит использовать функции filter + lambda. Возможно, упростит решением класс Counter модуля collections =)
