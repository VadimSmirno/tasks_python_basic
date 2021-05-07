class MyDict:  # TODO, родительский класс должен быть "словарь"
    # TODO, переопределить необходимо только метод get.
    def __init__(self,key,value):
        self.__key = key
        self.__value = value

    def __str__(self):
        return f'{self.__key} : {self.__value}'


    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

    def set_value(self,value):
        return self.__value==value
