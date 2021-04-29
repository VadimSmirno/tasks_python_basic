import random

students = []

class Student:

    def __init__(self, name, number_grupp, school_performance):
        self.name = name
        self.number_grupp = number_grupp
        self.school_performance = school_performance

    def print_info(self):
        print(f'{self.name} из группы № {self.number_grupp}: оценки за 5 предметов: {self.school_performance}')

    # def add_student(self, name, number_grupp, school_performance):
    #     self.students.append([name, number_grupp, sum(school_performance) / 5])


people = ['Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил', 'Никита']

for i_name in people:
    name, number_grupp, school_performance = i_name, random.randint(1, 10), [random.randint(1, 5) for _ in range(5)]
    # TODO, предлагаю создавать список для добавления студентов вне класса и добавлять в него сразу объекты класса Student()
    student = Student(name, number_grupp, school_performance)
    students.append([student.name,student.number_grupp,sum(school_performance) / 5])

print(students)

sort_lst = sorted(students, key=lambda k: k[2])
for i_info in sort_lst:
    print(f'Студент {i_info[0]} учится в группе № {i_info[1]}, средний бал по успеваемости: {i_info[2]}')
