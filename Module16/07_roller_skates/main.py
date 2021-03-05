skate_size_list = []
foot_size_list = []
count = 0
number_skates = int(input('Количество коньков: '))
for i_ns in range(1, number_skates +1):
    print('размер ',i_ns,'пары: ', end = '')
    skate_size = int(input())
    skate_size_list.append(skate_size)

number_people = int(input('\nКоличество людей: '))
for i_np in range (1,number_people+1):
    print ('Размер ноги', i_np,'человека: ', end = '')
    foot_size = int(input())
    foot_size_list.append(foot_size)

for _ in range (number_skates):
    if min(foot_size_list) <= min(skate_size_list):
        count += 1
        foot_size_list.remove(min(foot_size_list))
        skate_size_list.remove((min(skate_size_list)))
    elif min(foot_size_list) > min(skate_size_list):
        skate_size_list.remove((min(skate_size_list)))



print ('Наибольшее количество людей которые могут взять ролики:', count)