class ExampleClass:
    def __init__(self, value):
        if value % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(3)
try:
    print(example_object.a)
except AttributeError:
    print("Атрибут example_object.a не существует")

try:
    print(example_object.b)
except AttributeError:
    print("Атрибут example_object.b не существует")