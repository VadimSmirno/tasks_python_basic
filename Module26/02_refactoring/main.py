from collections.abc import Iterable

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def multiplication(list_1: list, list_2: list) -> Iterable[int]:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                yield 'Found!!!'


function_result = multiplication(list_1, list_2)
for i_result in function_result:
    print(i_result)

# зачёт!
