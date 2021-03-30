family_dict = {
    ('Петров', 'Иван') : 25,
    ('Петрова','Анна') : 24,
    ('Петров', 'Николай'): 62,

    ('Сидоров', 'Никита') : 35,
    ('Сидорова', 'Алина') : 34,
    ('Сидоров', 'Павел') : 10

}


surname = input('Введите фамилию семьи: ')
for i_person,age in family_dict.items():
    if i_person[0] == surname or i_person[0] == surname + 'а':
        print (i_person[0],i_person[1],age)
