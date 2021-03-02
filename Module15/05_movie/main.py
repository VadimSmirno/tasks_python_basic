films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = len(films)

favorite_films = []

# TODO, "while count_films != 0:" Правильно проверять "0", таким образом проверяем текст, проверяя 0 проверяем число =)
#  К сожалению, для python это 2 разных символа. Предлагаю попробовать реализовать
#  цикл while с возможностью выхода из цикла =)
for _ in range(1, len(films) + 1):
    interested_films = input('Введите название фильма: ')

    if interested_films in films:
        favorite_films.append(interested_films)
    else:
        print('Ошибка, такого фильма на сайте нет')

print('Любимые фильмы', favorite_films)


