line = input('Введите строку: ')
index = 0
count = 1
out = ''
while index< (len(line) - 1):
    if line[index] == line[index+1]:
        count += 1
    else:
        out = out + line[index] + str(count)
        count = 1
    index +=1
print(out+ line[index] + str(count))