class Date:

    def __init__(self):
        # TODO, предлагаю разбить дату на аргументы при запросе данных и сделать один или несколько обязательных параметров.
        self.date = None

    @classmethod
    def from_string(cls, date):
        lst_date = date.split('-')
        # TODO, возвращать необходимо объект класса Date
        return f'День: {lst_date[0]}\t' \
               f'Месяц: {lst_date[1]}\t' \
               f'Год: {lst_date[2]}\n'

    @classmethod
    def is_date_valid(cls, date):
        lst_date = date.split('-')
        number = int(lst_date[0])
        month = int(lst_date[1])
        year = int(lst_date[2])
        if 0 < number <= 31 and 0 < month <= 12 and year > 0:
            return True
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
