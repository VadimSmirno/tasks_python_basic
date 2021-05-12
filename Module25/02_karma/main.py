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

    call_or_not_error = random.randint(1,10)
    if call_or_not_error == 1:
        raise random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    else:
        return random.randint(1,7)

number_karma = 0
while number_karma < 500:

    try:
        function_result = one_day()
        number_karma += function_result

    except (KillError,DrunkError,CarCrashError,GluttonyError,DepressionError) as err:
        print (err)
        with open('karma.log', 'a',encoding='UTF-8') as fail:
             fail.write(f'карма нарушена {err}\n')
    print(f'Уровень кармы {number_karma}')



