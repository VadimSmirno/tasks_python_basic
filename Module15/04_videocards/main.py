number_video_cards = int(input('Введите количество видеокарт: '))
old_list_video_cards = []
new_list_video_cards = []

for index in range (1,number_video_cards+1):

    print ('Видеокарта №', index, ':', end = '')
    version_video_cards = int(input())
    old_list_video_cards.append(version_video_cards)

for num in  old_list_video_cards:
    # TODO, как нам определить максимальное число без функции max? =)
    if num < max(old_list_video_cards):
        new_list_video_cards.append(num)





print('Старый список видеокарт: ',old_list_video_cards )
print('Новый список видеокарт: ',new_list_video_cards )


