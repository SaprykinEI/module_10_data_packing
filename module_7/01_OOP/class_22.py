class SampleClass:

    def __init__(self, val):
        self.val = val


obj1 = SampleClass(0)
obj2 = SampleClass(2)
obj3 = obj1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj1 is obj3)