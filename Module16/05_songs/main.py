violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
summ = 0
number_songs = int(input('Сколько песен выбрать? '))
for i_num in range (1,number_songs+1):
    print('Название',i_num,'песни:', end = '')
    name_songs = input()
    for i in range(len((violator_songs))):
        if violator_songs [i][0] == name_songs:
            summ += violator_songs[i][1]
print('Общее время звучания песен',round(summ,2))

