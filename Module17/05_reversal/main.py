text = input('Введите текст: ')
stop = text.index('h')
start = text[::-1].index('h')
print(text [:stop+1] + text[-start - 2:stop:-1] + text [-start-1:])

