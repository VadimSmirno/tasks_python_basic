class Person:

    def __init__(self,name,surname,age):
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

    def __str__(self):
        f'{self.get_name(),self.get_surname()} возраст: {self.get_age()} '




class Manager(Employee):
   def selary(self):
       return 13000


class Agent(Employee):
    def __init__(self, name, surname, age,volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def selary_agent(self):
        return  5000 + self.volume_of_sales*0.05


class Worker(Employee):
    def __init__(self, name, surname, age,opening_hours):
        super().__init__(name, surname, age)
        self.opening_hours = opening_hours

    def selary_worker(self):
        return 100 * self.opening_hours

maneger = Manager('Путя', 'Иванов', 23)
