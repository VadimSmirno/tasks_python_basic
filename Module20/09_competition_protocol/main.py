score_table = {}
number = int(input('Сколько записей вносится в протокол?'))
for time in range(1,number +1):
    print (time, 'запись:', end='')
    ball, name = input().split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]
scores = list(score_table.items())

def score_key(key):
    return key[1][0]- key[1][1]

scores.sort(key=score_key,reverse=True)
for num in range(3):
    print (num+1, 'место', scores[num][0], scores[num][1][0])
