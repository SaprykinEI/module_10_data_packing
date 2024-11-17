def enqueue(queue, data):
    if data == "очередь пуста":
        return
    queue.append(data)


def dequeue(queue):
    # if len(queue) == 0:
    if not queue:
        return f"очередь пуста"
    return queue.pop(0)

def peek_first(queue):
    if not queue:
        return f"очередь пуста"
    return queue[0]

def peek_last(queue):
    if not queue:
        return f"очередь пуста"
    return queue[-1]


def size(queue):
    return len(queue)


queue_1 = []
queue_2 = []

enqueue(queue_1, 'data_1')
enqueue(queue_1, 'data_2')
enqueue(queue_1, 'data_3')
enqueue(queue_1, 'data_4')
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
enqueue(queue_2, dequeue(queue_1))
print(size(queue_2))
print(peek_first(queue_2))
print(peek_last(queue_2))
print(queue_2)