import itertools

number = [0,1,2,3,4,5,6,7,8,9]

count = 0
for item in itertools.combinations_with_replacement(number,4):
    count += 1
    print(item)

print(count)

# Пожалуйста, обратите внимание, вариант (9, 9, 9, 9) тоже должен быть доступен.
# TODO всего должно получиться 10000 вариантов. =) пока что, получается 715
#  Предлагаю попробовать найти функцию модуля itertools, при помощи которой мы сможем учесть все варианты. =)
