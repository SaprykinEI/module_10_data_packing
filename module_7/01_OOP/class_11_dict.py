class ExampleClass:
    __counter = 0

    def __init__(self, first=1):
        self.__first = first
        ExampleClass.__counter +=1

    @classmethod
    def get_counter(cls):
        return cls.__counter

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
example_object_4 = ExampleClass(5)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
print(example_object_4.__dict__, example_object_4._ExampleClass__counter)
print(ExampleClass.get_counter())
print()

print(example_object_1.__dict__, example_object_1.get_counter())
print(example_object_2.__dict__, example_object_2.get_counter())
print(example_object_3.__dict__, example_object_3.get_counter())
print(example_object_4.__dict__, example_object_4.get_counter())

