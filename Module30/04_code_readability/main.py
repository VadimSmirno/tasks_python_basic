result = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), range(2, 10000)))
print(result)

lst = []
for num in range(2, 1001):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        lst.append(num)

print(lst)

# зачёт!
