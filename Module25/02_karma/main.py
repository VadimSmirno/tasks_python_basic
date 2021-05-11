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
    # TODO, выбирать нужное исключение лучше в блоке if, таким образом, сократим количество действий для python в ряде случаев.
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
        # TODO, предлагаю добавить необходимую кодировку при открытии файла, иначе, для пользователей Windows
        #  не очень понятно, что записывается в файл.
        with open('karma.log', 'a') as fail:
             fail.write(f'карма нарушена {err}\n')
    else:
        # TODO, эти действия лучше делать в блоке try.
        #  аким образом блок lse будет лишним и код будет в одном месте =)
        number_karma += function_result
    print(f'Уровень кармы {number_karma}')



