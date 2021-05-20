class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node [{str(self.value)}]'


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList[]'

    def append(self, elem):
        # TODO, стоит увеличить длину до добавления.
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index):
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1  # TODO, лишнее действие.
                return

        while cur_node is not None:
            if cur_index == index:  # TODO, правильно проверять, если строго больше
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        # TODO, если текущий Node None, то выходим из метода.

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index):

        # TODO, если текущая длина равна 0 или меньше индекса элемента, из метода стоит выйти =)

        node = self.head
        curr_index = 0
        while curr_index <= index:
            if curr_index == index:
                return node.value
            curr_index += 1
            node = node.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
print()
# my_list.remove(0)
print(my_list.get(2))
print(my_list.get(3))
print(my_list)
