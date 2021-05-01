import random

students = []

class Student:

    def __init__(self, name, number_grupp, school_performance):
        self.name = name
        self.number_grupp = number_grupp
        self.school_performance = school_performance

    def print_info(self):
        print(f'{self.name} из группы № {self.number_grupp}: оценки за 5 предметов: {self.school_performance}')



people = ['Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил', 'Никита']

for i_name in people:
    name, number_grupp, school_performance = i_name, random.randint(1, 10), [random.randint(1, 5) for _ in range(5)]
    student = Student(name, number_grupp, sum(school_performance)/5)
    students.append(student)


sort_lst = sorted(students, key=lambda k: k.school_performance)
for i_info in sort_lst:
    print(f'Студент {i_info.name} учится в группе № {i_info.number_grupp}, средний бал по успеваемости: {i_info.school_performance}')
