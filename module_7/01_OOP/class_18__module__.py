class Classy:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    print(Classy.__module__)
    obj = Classy('ClassyObj')
    print(obj.__module__)