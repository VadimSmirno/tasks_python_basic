films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = len (films)

favorite_films = []
while count_films != 0:
    interested_films = input('Введите название фильма: ')
    count_films -= 1

    if interested_films in films:
        favorite_films.append(interested_films)
    else:
        print('Ошибка, такого фильма на сайте нет')


print ('Любимые фильмы', favorite_films)

