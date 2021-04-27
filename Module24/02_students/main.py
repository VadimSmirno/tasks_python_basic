import random

class Student:


    def __init__(self,name,number_grupp,school_performance):
        self.name = name
        self.number_grupp = number_grupp
        self.school_performance = school_performance
        self.students = []

        print(f'{name} из группы № {number_grupp}: оценки за 5 предметов: {school_performance}')



people = ['Дмитрий', 'Максим', 'Сергей', 'Андрей','Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил', 'Никита']

for i_name in people:
    name, number_grupp, school_performance = i_name, random.randint(1, 10),[random.randint(1, 5) for _ in range(5)]
    student = Student(name,number_grupp,school_performance)
