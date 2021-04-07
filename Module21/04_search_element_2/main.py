site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац',
            'a': {
                'r': '45'
            }
        }

    }
}


def find_key(struct, key, count):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            if count <= 0:
                return print('На этом уровне ключ не найден')
            result = find_key(sub_struct, key, count - 1)
            if result:
                break

    else:
        result = None
    return result


user_key = input('Какой ключ ищем? ')
count = int(input('Какую ввести максимальную глубину — уровень? '))
value = find_key(site, user_key, count)

if value:
    print(value)
else:
    print('Такого ключа в структуре словаря нет')

# TODO, в целом, решено правильно, но на уровне 2 ключа h2 нет. (Он есть на уровне 3)
#  Но, мы пока что находим =)
