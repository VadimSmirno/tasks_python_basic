import collections

# def can_be_poly(str):
#     str_lower = str.lower()
#     dct_count = defaultdict(int)
#     for symbol in str_lower:
#         if ord(symbol) >= 97 and ord(symbol) <=122:
#             dct_count[symbol] += 1
#     middle = ''
#     for symbol in dct_count:
#         if middle and dct_count[symbol] % 2 == 1:
#             return False
#         elif dct_count[symbol] % 2 == 1:
#             middle = symbol
#     return  True

def can_be_poly(str):
    result = filter(lambda x : x % 2 != 0,collections.Counter(str.replace(' ','').lower()).values())
    if len(list(result))> 1:
        return False
    else:
        return True
#
print(can_be_poly('ab aBc'))
print(can_be_poly('abbbc'))


