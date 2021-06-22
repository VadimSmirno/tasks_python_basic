import re

number_car = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

auto = re.findall(r'\b\D{1}\d{3}\D{2}\d{3}',number_car)
taxi = re.findall(r'\D{2}\d{5,6}',number_car)

print(f'Список номеров частных автомобилей: {auto}')
print(f'Список номеров такси: {taxi}')