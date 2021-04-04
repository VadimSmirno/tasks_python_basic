def min_len(string, cortege):
    return min(len(string), len(cortege))


string = 'abcd'
cortege = (10, 20, 30, 40, 52)

result = ((string[i_sym], cortege[i_sym]) for i_sym in range(min_len(string, cortege)))
print(result)
for element in result:
    print(element)

# зачёт!
