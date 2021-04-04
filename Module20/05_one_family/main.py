family_dict = {
    ('Петров', 'Иван'): 25,
    ('Петрова', 'Анна'): 24,
    ('Петров', 'Николай'): 62,

    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10

}

surname = input('Введите фамилию семьи: ')
for i_person, age in family_dict.items():
    #  + "a" в решении лишнее. Возможно проверки "surname in i_person " будет достато =)
    if surname in i_person or surname + 'а' in i_person:
        print(i_person[0], i_person[1], age)

# зачёт!
