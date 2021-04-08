def sum1(lst):
    total = 0
    for element in lst:
        if type(element) == type([]):
            total += sum1(element)
        else:
            total += element
    return total


print(sum1([[1, 2, [3, [[[10]]]]], [1], 3]))
print(sum1((1, 2, 3, 4, 5)))

# зачёт!
