films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = len(films)

favorite_films = []

interested_films = input('Введите название фильма: ')
while interested_films != 'end':
    if interested_films in films:
        favorite_films.append(interested_films)
    else:
        print('Ошибка, такого фильма на сайте нет')
    interested_films = input('Введите название фильма: ')

print('Любимые фильмы', favorite_films)

# зачёт!
