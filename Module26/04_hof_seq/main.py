class Hofstadter:
    def __init__(self, lst):
        self.lst = lst[:]

    def __next__(self):
        try:
            q = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
            self.lst.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self



hofstadter = Hofstadter([1,1])
print ([next(hofstadter) for  _ in range(10)])
