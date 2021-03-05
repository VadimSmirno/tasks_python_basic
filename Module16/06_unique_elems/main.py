
first_list = []
second_list = []
for i_fl in range (1,4):
    print('Введите ',i_fl,'-е  число в первый список: ', end = '')
    number = int(input())
    first_list.append(number)
print ()
for i_sl in range (1,8):
    print('Введите ',i_sl,'-е  число во второй список: ', end = '')
    number = int(input())
    second_list.append(number)

new_list = []
new_list.extend(first_list)
new_list.extend((second_list))


for index in new_list:
    while new_list.count(index) > 1:
        new_list.remove(index)
print (new_list)
