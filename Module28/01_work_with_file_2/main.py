
class File:
    """"
    Класс при попытке открыть не существующий файл
    автоматически создается и открывается этот файл 
    в режиме записи
    Также при выходе подавляются все исключения связанные
    с файлами
    """""

    def __init__(self, file_name: str, method: str) -> None:
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        try:
            self.file_obj = open(self.file_name, self.method, encoding='UTF-8')
        except Exception:
            self.file_obj = open(self.file_name, 'w', encoding='UTF-8')
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file_obj.close()
        if exc_type is FileNotFoundError and FileExistsError and EOFError \
                and IsADirectoryError:
            return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!\n')

# зачёт!
