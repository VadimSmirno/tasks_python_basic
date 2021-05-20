## Задача 6. Односвязный список
Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать Односвязный список.

Связный список — это структура данных, которая состоит из элементов, зовущихся узлами. В узлах хранятся данные, а между собой узлы соединены связями. Связь – это ссылка на следующий или предыдущий элемент списка.

![task_06_pic](linkedlist.png)

В односвязном списке связь - это ссылка только на следующий элемент. То есть в нём можно передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Питона (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:
- append - добавление элемента в конец списка
- get - получение элемента по индексу
- remove - удаление элемента по индексу

Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла

####Пример основной программы:
````python
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
````

####Результат:
````
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]
````

