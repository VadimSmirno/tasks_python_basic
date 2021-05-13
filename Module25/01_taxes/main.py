class Property:

    def __init__(self, worth):
        self.worth = worth

    # , пожалуйста, оставьте только 1 метод для расчёта налога.
    # def tax_calculation(self):
    #     result = self.worth/coefficient
    # , метод возможно лишний, т.к. заменяем всего 1 строку кода.
    #  или, можно перенести в него возврат =)

    # return result

    def print_info(self, result):
        print(f'налог составил: {result}')


class Apartment(Property):
    # , если метод не меняется, то переопределять его не нужно =)
    #  Предлагаю в наши методы добавить коэффициенты для расчёта 1000, 500 и 200
    def tax_calculation(self, coefficient=1000):
        result = self.worth / coefficient
        self.print_info(result)
        return result


class Car(Property):

    def tax_calculation(self, coefficient=500):
        result = self.worth / coefficient
        self.print_info(result)
        return result


class CountryHouse(Property):

    def tax_calculation(self, coefficient=200):
        result = self.worth / coefficient
        self.print_info(result)
        return result


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
        result = apartment.tax_calculation()
        if not check(result, money):
            break
        money -= result
    elif property == 'машина':
        car = Car(worth=price)

        result_car = car.tax_calculation()
        if not check(result_car, money):
            break
        money -= result_car
    elif property == 'дача':
        country_house = CountryHouse(worth=price)

        result_country_house = country_house.tax_calculation()
        if not check(result_country_house, money):
            break
        money -= result_country_house
else:
    print(f'Налог уплачен осталось средств {money}')

# зачёт!
# зачёт!
