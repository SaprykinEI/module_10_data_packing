class MyClass:
    pass

my_obj = MyClass()
my_obj.a = 1
my_obj.b = 2
my_obj.i = 3
my_obj.ireal = 3.5
my_obj.integer = 4
my_obj.z = 5


def inc_ints_i(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(my_obj.__dict__)
inc_ints_i(my_obj)
print(my_obj.__dict__)