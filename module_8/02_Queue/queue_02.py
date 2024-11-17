class Queue:
    def __init__(self, queue=None):
        if queue is None:
            self.__queue = []
        else:
            self.__queue = queue

    def enqueue(self, data):
        if data == "Очередь пуста":
            return
        self.__queue.append(data)

    def dequeue(self):
        if not self.__queue:
            return "Очередь пуста"
        return self.__queue.pop(0)

    def peek_first(self):
        if not self.__queue:
            return "Очередь пуста"
        else:
            return self.__queue[0]

    def peek_last(self):
        if not self.__queue:
            return "Очередь пуста"
        else:
            return self.__queue[-1]

    def size(self):
        return len(self.__queue)


if __name__ == '__main__':
    my_queue = Queue([])
    my_queue.enqueue('data_1_obj')
    my_queue.enqueue('data_2_obj')
    my_queue.enqueue('data_3_obj')
    my_queue.enqueue('data_4_obj')
    print(my_queue.size())
    print(my_queue.peek_first())
    print(my_queue.peek_last())
    print(my_queue.size())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())