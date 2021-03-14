import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [first_team[index] if first_team[index] > second_team[index]
           else second_team[index] for index in range(20)]
print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители турнира: ', winners)

# зачёт!
