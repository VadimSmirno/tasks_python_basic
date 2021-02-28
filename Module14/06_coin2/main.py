def coin():
    print('Введите координаты монетки')
    x = float(input('X: '))
    y = float(input('Y: '))
    radius = float(input('Введите радиус '))
    if x < radius and y < radius:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


coin()

# зачёт!
