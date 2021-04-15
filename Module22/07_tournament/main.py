
first_tour = open('first_tour.txt','r')
print('Содержимое файла first_tour.txt: \n'+first_tour.read())
first_tour = open('first_tour.txt','r')
total_lst = []
number = int (first_tour.readline())
for i_sym in first_tour:
    lst = i_sym.split()
    if int(lst[2]) > number:
        lst = [lst[0],lst[1], int(lst [2])]

        total_lst.append(lst)
winners = len(total_lst)
count = 1
second_tour = open('second_tour.txt', 'a')
second_tour.write(str(winners)+'\n')
for i_elem in sorted(total_lst):
    second_tour.write (f'{count}) {i_elem[1][0]}. {i_elem[0]} {i_elem[2]}\n')
    count+=1

print ('\nСодержимое файла second_tour.txt:')
second_tour = open('second_tour.txt', 'r')
print (second_tour.read())
first_tour.close()
second_tour.close()
