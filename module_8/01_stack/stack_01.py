# def push(val):
#     stack.append(val)
#
# def pop():
#     val = stack.pop()
#     return val
#
# stack = []
# push(3)
# push(2)
# push(1)
#
# print(pop())
# print(pop())
# print(pop())


def push(stack, val):
    stack.append(val)

def pop(stack):
    if stack:
        val = stack.pop()
    else:
        return "Stack is empty"
    return val

my_stack = []
push(my_stack, 3)
push(my_stack,2)
push(my_stack,1)

print(pop(my_stack))
print(pop(my_stack))
print(pop(my_stack))
print(pop(my_stack))


