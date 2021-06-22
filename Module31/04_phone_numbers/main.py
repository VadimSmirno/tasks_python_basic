import re

telephone_number = ['9999999999', '999999-999', '99999x9999']

count = 1
for  i_number in telephone_number:
    if re.match(r'[8-9]{1}[0-9]{9}', i_number) and len(i_number) == 10:
        print(f'{count} номер: всё в порядке')
    else:
        print (f'{count} номер: не подходит')
    count += 1