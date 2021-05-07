class Property:

    def __init__(self,worth):
        self.worth = worth


    # TODO, пожалуйста, оставьте только 1 метод для расчёта налога.
    def tax_calculationApartment(self):
        result = self.worth/1000
        # TODO, метод возможно лишний, т.к. заменяем всего 1 строку кода.
        #  или, можно перенести в него возврат =)
        self.print_info(result)
        return result

    def tax_calculationCar(self):
        result = self.worth / 200
        self.print_info(result)
        return result

    def tax_calculationCountryHouse(self):
        result = self.worth/500
        self.print_info(result)
        return result

    def print_info(self,result):
        print (f'налог составил: {result}')


class  Apartment(Property):
    # TODO, если метод не меняется, то переопределять его не нужно =)
    #  Предлагаю в наши методы добавить коэффициенты для расчёта 1000, 500 и 200
    def __init__(self,worth):
        super().__init__(worth)

class  Car(Property):
    def __init__(self,worth):
        super().__init__(worth)

class  CountryHouse(Property):
    def __init__(self,worth):
        super().__init__(worth)


def check(res, money):
    if res < money:
        money -= result
        print('Налог оплачен, осталось {}'.format(money))
        return True
    else:
        print('У Вас недостаточно средств')
        return False

money = int(input('Какими средствами располагаете? '))
for _ in range(3):
    property = input('За какое имущество хотите заплатить налог? ').lower()
    price = int(input(f'Какова стоимость {property}? '))
    if property == 'квартира':
        apartment = Apartment(worth=price)
        result = apartment.tax_calculationApartment()
        if not check(result,money):
            break
        money-=result
    elif property == 'машина':
        car = Car(worth=price)
        car.tax_calculationCar()
        result_car = car.tax_calculationCar()
        if not check(result_car, money):
            break
        money -= result_car
    elif property == 'дача':
        country_house = CountryHouse(worth=price)
        country_house.tax_calculationCountryHouse()
        result_country_house = country_house.tax_calculationCountryHouse()
        if not check(result_country_house,money):
            break
        money -= result_country_house
else:
    print (f'Налог уплачен осталось средств {money}')





