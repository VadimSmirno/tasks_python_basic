country_dict = {}

number_country = int(input('Кол-во стран: '))
for i_country in range(1, number_country + 1):
    print(f'{i_country} страна: ', end='')
    country = input('').split()
    for i_citie in range(1, len(country)):
        country_dict[country[i_citie]] = country[0]
print(country_dict)

for num in range(1, 4):
    print(f'{num}. город: ', end='')
    citie = input('')
    if country_dict.get(citie) == None:
        print(f'по городу {citie} данных нет\n')
    else:
        print(f'Город {citie} расположен в стране {country_dict.get(citie)}\n')

# зачёт!
