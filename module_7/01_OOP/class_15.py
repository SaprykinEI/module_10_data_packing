class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

class ExampleClass:
    a = 1

    def __init__(self):
        self.b = 2


example_object = ExampleClass()
print(hasattr(example_object, 'a'))
print(hasattr(example_object, 'b'))
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))