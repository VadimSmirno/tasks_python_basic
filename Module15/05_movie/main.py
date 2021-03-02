films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = len(films)

favorite_films = []

# TODO, таким образом первый фильм не добавляется в список любимы, если есть в основном списке =)
interested_films = input('Введите название фильма: ')
while interested_films != 'end':
    # TODO, возможно этот запрос стоит реализовать после проверки.
    interested_films = input('Введите название фильма: ')

    if interested_films in films:
        favorite_films.append(interested_films)
    else:
        print('Ошибка, такого фильма на сайте нет')

print('Любимые фильмы', favorite_films)


