class Classy:
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


classy_object = Classy()
print(classy_object.__dict__)
print(Classy.__dict__)