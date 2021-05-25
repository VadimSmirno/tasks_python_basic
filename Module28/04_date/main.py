class Date:

    def __init__(self,number,month,year):
        self.number = number
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.number}\t' \
               f'Месяц: {self.month}\t' \
               f'Год: {self.year}\n'

    @classmethod
    def from_string(cls, date):
        lst_date = date.split('-')
        result = cls(lst_date[0],lst_date[1],lst_date[2])
        return result

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
