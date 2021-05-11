class Steck:
    def __init__(self):
        self.__lst = []

    def __str__(self):
        return '; '.join(self.__lst)

    def push(self, elem):
        self.__lst.append(elem)

    def pop(self):
        if len(self.__lst) == 0:
            return None
        return self.__lst.pop()


class TaskManager:

    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)} {self.task[i_priority]}\n')
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Steck()
        self.task[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# зачёт!
