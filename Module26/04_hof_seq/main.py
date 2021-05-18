class Hofstadter:
    def __init__(self, lst):
        self.lst = lst
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.lst):
            self.count += 1
            q = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
            self.lst.append(q)
            return q
        else:
            raise StopIteration()


hofstadter = Hofstadter([1, 1])
print([next(hofstadter) for _ in range(15)])


def hofstadter_generator(lst):
    new_lst = lst
    while True:
        q = lst[-lst[-1]] + lst[-lst[-2]]
        new_lst.append(q)
        yield q


result = hofstadter_generator([1, 1])
print([next(result) for i in range(10)])

# зачёт!
