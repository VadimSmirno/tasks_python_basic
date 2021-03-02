def max_num (old_list_video_cards):
    max_num = 0
    for index in old_list_video_cards:
        if index > max_num:
            max_num = index
    return max_num


number_video_cards = int(input('Введите количество видеокарт: '))
old_list_video_cards = []
new_list_video_cards = []

for index in range (1,number_video_cards+1):
    print ('Видеокарта №', index, ':', end = '')
    version_video_cards = int(input())
    old_list_video_cards.append(version_video_cards)

for num in  old_list_video_cards:

    if num < max_num (old_list_video_cards) :
        new_list_video_cards.append(num)





print('Старый список видеокарт: ',old_list_video_cards )
print('Новый список видеокарт: ',new_list_video_cards )


