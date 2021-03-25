violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
time_songs = 0
number_songs = int(input('Количество песен: '))
for i_songs in range(1, number_songs + 1):
    print('Название', i_songs, 'пестни: ', end='')
    songs = input('')
    time_songs += violator_songs[songs]
print('Общее время звучания песне: ', round(time_songs, 2))

# зачёт!
