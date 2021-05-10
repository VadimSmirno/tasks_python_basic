import random


class KillError(Exception):

    def __str__(self):
       return 'Убил комара'

class DrunkError(Exception):

    def __str__(self):
        return 'Выпил'

class CarCrashError(Exception):

    def __str__(self):
        return 'Пьяный за рулем'

class GluttonyError(Exception):

    def __str__(self):
        return 'Возжелал того, чего желать не стоит'

class DepressionError(Exception):

    def __str__(self):
        return 'Впал в депрессию'



def one_day():

    return (random.randint(1, 7))
    # TODO, эта функция должна или вызывать исключение или возвращать количество кармы.
    #  предлагаю хранить исключения в списке, в таком случае какой метод модуля random
    #  может помочь получить случайный элемент списка? =)

number_karma = 0
while number_karma < 500:

    number_karma += one_day()
    number_exception = random.randint(1,50)

    try:
        if number_exception == 1:
            print ('Карма нарушена')
            raise KillError
        elif number_exception == 10:
            raise DrunkError
        elif number_exception == 20:
            raise CarCrashError
        elif number_exception == 30:
            raise GluttonyError
        elif number_exception == 40:
            raise DepressionError

    except (KillError,DrunkError,CarCrashError,GluttonyError,DepressionError) as err:
        with open('karma.log', 'a') as fail:
            fail.write(f'карма нарушена {err}\n')
    print(f'Уровень кармы {number_karma}')



