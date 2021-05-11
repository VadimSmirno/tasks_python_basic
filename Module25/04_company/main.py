class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def print_info(self):
        print(f'{self.get_name()} {self.get_surname()} возраст: {self.get_age()} ')


class Manager(Employee):
    def __init__(self, name, surname, age, selary):
        super().__init__(name, surname, age)
        self.selary = selary

    # , стоит определить метод init и в нём создать аргумент "заработная плата"
    #  в selary предлагаю возвращать именно этот аргумент )

    def selary_manager(self):
        return self.selary


class Agent(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.selary = 5000
        self.percent = 5

    def selary_agent(self):
        return self.selary + self.selary * self.percent / 100


class Worker(Employee):
    def __init__(self, name, surname, age, opening_hours):
        super().__init__(name, surname, age)
        self.opening_hours = opening_hours

    def selary_worker(self):
        return 100 * self.opening_hours


maneger1 = Manager(name='Петя', surname='Иванов', age=23, selary=13000)
maneger2 = Manager(name='Коля', surname='Сидоров', age=21, selary=13000)
maneger3 = Manager(name='Ваня', surname='Петров', age=22, selary=13000)
agent = Agent(name='Лена', surname='Петрова', age=25)
agent1 = Agent(name='Оля', surname='Козлова', age=26)
agent2 = Agent(name='Саша', surname='Цветкова', age=24)
worker = Worker(name='Володя', surname='Козлов', age=23, opening_hours=135)
worker2 = Worker(name='Наташа', surname='Волкова', age=33, opening_hours=175)
worker3 = Worker(name='Володя', surname='Серов', age=23, opening_hours=152)
lst = [maneger1, maneger2, maneger3, agent, agent1, agent2, worker, worker2, worker3]

for i_objekt in lst:
    print(i_objekt.print_info())

# зачёт!
