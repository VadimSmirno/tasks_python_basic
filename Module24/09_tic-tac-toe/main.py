class Toyota:           # это класс

    def __init__(self):
        self.color = 'белый'
        self.price = '1234'         # это атрибуты класса
        self.max_speed = '200 км/ч'

toyota_LC200 = Toyota()  # это объект класса он же экземпляр класса


class Toyota2:  # это класс

    def __init__(self,color,price,max_speed):
        self.color = color
        self.price = price  # это атрибуты класса
        self.max_speed = max_speed
        self.toyota_LC200 = Toyota()     # передали класс Toyota в класс Toyota2

    def start(self):
        print ('Заводим мотор') # это метод класса
        print(self.price) # обращаемся к аргументам(атрибутам) класса внутри класса

    def stop(self):    # это метод класса
        print ('Глушим ммотор')
        print(self.max_speed) # обращаемся к аргументам(атрибутам) класса внутри класса

toyota_camry = Toyota2('белый', '2 млн','250 км/ч')     # экземпляр класса
toyota_RAV4 = Toyota2('Черный', '1,5 млн','180 км/ч')    # экземпляр класса