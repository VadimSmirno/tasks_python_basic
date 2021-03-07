
def josephus(ls, skip):
    skip -= 1
    idx = skip
    while len(ls) > 1:
        if idx+1 > len(ls):
            idx %= len(ls)
        print(ls.pop(idx),"выбывает")
        idx = (idx + skip) % len(ls)
        print(idx,"Это IDX")
    print('survivor: ', ls[0])

ls = [1,2,3,4,5]
josephus(ls,7)