students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for i_key, i_value in students.items():
    id_student_age = [i_value['name'], i_value['surname'], i_value['age']]
    print(id_student_age)


def hobby_len_surname(dict):
    lst = []
    string = 0
    for key, value in dict.items():
        lst.extend(value['interests'])
        string += len(value['surname'])

    return lst, string


my_lst, total_len_surname = hobby_len_surname(students)
print(my_lst, total_len_surname)

# зачёт!
# зачёт!
