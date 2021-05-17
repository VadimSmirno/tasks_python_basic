class Hofstadter:
    def __init__(self, lst):
        self.lst = lst
        # TODO, предлагаю попробовать решить без списка
        #  Генераторы не должны хранить в себе полные массивы с данными.
        #  Должны производить расчёт и возвращать данные постепенно.

    def __next__(self):
        try:
            q = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
            self.lst.append (q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        # TODO, возможно iter лучше перенести под init, т.к. он тоже содержит список необходимых аргументов.
        #  Стоит добавить переменную счётчик и отталкиваться в решении от неё. Изначально равную "0".
        return self



hofstadter = Hofstadter([1,1])
print  ([next(hofstadter) for _ in range (10)])


def hofstadter_generator(lst):
    new_lst = lst
    while True:
        # TODO, ловить ошибки не нужно. Необходимо их избегать =)
        try:
            q = lst[-lst[-1]] + lst[-lst[-2]]
            new_lst.append(q)
            yield q
        except IndexError:
            return
result =  hofstadter_generator([1,1])
print ([next(result) for i in range (10)])
