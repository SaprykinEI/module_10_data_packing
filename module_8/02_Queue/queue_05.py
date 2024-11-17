class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:

    def __init__(self, head=None, tail=None, max_length=5):
        self.head = head
        self.tail = tail
        self.max_length = max_length

    def enqueue(self, data):
        if self.is_full():
            return "Очередь заполнена"
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data

    def get_queue_length(self):
        items_count = 0
        current = self.head  # Используем временную переменную
        while current:
            items_count += 1
            current = current.next_node
        return items_count

    def show_queue(self):
        current = self.head  # Используем временную переменную
        while current:
            print(current.data)
            current = current.next_node

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def is_full(self):
        if self.max_length == self.get_queue_length():
            return True
        return False







my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue('item_1')
my_queue.enqueue('item_2')
print(my_queue.get_queue_length())
print(my_queue.is_full())
my_queue.enqueue('item_3')
my_queue.enqueue('item_4')
my_queue.enqueue('item_5')
my_queue.enqueue('item_6')

print(my_queue.get_queue_length())

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
