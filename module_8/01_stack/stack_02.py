class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        try:
            val = self.__stack_list.pop()
        except IndexError:
            return "Stack is empty"
        return val

    def get_stack(self):
        return self.__stack_list


stack_object_1 = Stack()
stack_object_2 = Stack()
stack_object_1.push(3)
stack_object_1.push(2)
stack_object_1.push(1)
stack_object_2.push(stack_object_1.pop())
stack_object_2.push(stack_object_1.pop())
stack_object_2.push(stack_object_1.pop())


print(stack_object_2.get_stack())
print(stack_object_2.pop())
print(stack_object_2.pop())
print(stack_object_2.pop())
print(stack_object_2.pop())
