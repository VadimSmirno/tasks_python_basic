from collections.abc import Iterable

number = int(input('Введите число '))

def print_result(iter_objekt:Iterable) ->None:
    for i_square in iter_objekt:
        print(i_square, end=' ')

square = (num**2 for num in range(1,number+1)) # генераторное выражение
print_result(square)
print('Результат генераторного выражения')



def sguare(num:int) -> Iterable[int]:                            # генератор
    for i_square in range(1,num+1):
        yield i_square ** 2

function_result = sguare(number)
print_result(function_result)
print ('Результат генератора')


class Square:                               # итератор
    def __init__(self,num:int) -> None:
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self)->int:

        if self.count < self.num:
            self.count += 1
            return self.count**2
        else:
            raise StopIteration


square_iter = Square(number)
print_result(square_iter)
print ('Результат итератора')



