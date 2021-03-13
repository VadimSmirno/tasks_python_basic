first_class = []
second_class = []
first_class.extend(list(range(160, 177, 2)))
second_class.extend(list(range(162, 181, 3)))
new_list = []

print(first_class)
print(second_class)

count_first_class = 0
count_second_class = 0
while count_first_class < len(first_class) and count_second_class < len(second_class):
    if first_class[count_first_class] <= second_class[count_second_class]:
        new_list.append(first_class[count_first_class])
        count_first_class += 1
    else:
        new_list.append(second_class[count_second_class])
        count_second_class += 1
if count_first_class < len(first_class):
    for index in range(count_first_class, len(first_class)):
        new_list.append(first_class[index])
elif count_second_class < len(second_class):
    for index in range(count_second_class, len(second_class)):
        new_list.append((second_class[index]))
print(new_list)
