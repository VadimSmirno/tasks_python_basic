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
    error = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    call_or_not_error = random.randint(1,10)
    if call_or_not_error == 1:
        raise error
    else:
        return random.randint(1,7)

number_karma = 0
while number_karma < 500:

    try:
        function_result = one_day()

    except (KillError,DrunkError,CarCrashError,GluttonyError,DepressionError) as err:
        print (err)
        with open('karma.log', 'a') as fail:
             fail.write(f'карма нарушена {err}\n')
    else:
        number_karma += function_result
    print(f'Уровень кармы {number_karma}')



