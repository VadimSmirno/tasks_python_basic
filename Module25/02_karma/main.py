import random


class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    # TODO, если определить метод str, то при записи текст можно не указывать и исключения сможем ловить группой.
    pass



def one_day():
    # TODO, функция должна или вызывать случайное исключение, или возвращать случайное количество кармы.
    return (random.randint(1, 7),random.randint(1, 50))

number_karma = 0
while number_karma < 500:
    # TODO, стоит подумать, как запускать функцию только 1 раз. =)
    number_karma += one_day()[0]
    number_exception = one_day()[1]

    try:
        if number_exception == 1:
            print ('Карма нарушена')
            raise KillError ('Убил комара')
        elif number_exception == 10:
            raise DrunkError ('Выпил')
        elif number_exception == 20:
            raise CarCrashError('Пьяный за рулем')
        elif number_exception == 30:
            raise GluttonyError('Возжелал того, чего желать не стоит')
        elif number_exception == 40:
            raise DepressionError ('Впал в депрессию')

    except (KillError,DrunkError,CarCrashError,GluttonyError,DepressionError) as err:
        with open('karma.log', 'a') as fail:
            fail.write(f'карма нарушена {err}\n')
    print(f'Уровень кармы {number_karma}')



