import itertools

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in itertools.product(number, repeat=4):
    print(item)

# зачёт!
