import timeit

res = timeit.timeit("'-'.join([str(num) for num in range(10**3)])", number=10000)

res2 = timeit.timeit ("'-'.join(list(map(lambda x: str(x),[number for number in range(100)])))", number=1000)
print(res)
print (res2)