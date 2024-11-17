class Animal:

    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"Животное {self.name} дышит"


class Fish(Animal):

    def __init__(self, name, specie):
        # Animal.__init__(name)
        super().__init__(name)
        self.specie = specie


    def breathe(self):
        result = super().breathe()
        return  f"{result}, это {self.specie} дышит жабрами"


    def swim(self):
        return f"{self.name}, {self.specie} умеет плавать"


class Lion(Animal):

    def __init__(self, name, specie):
        # Animal.__init__(name)
        super().__init__(name)
        self.specie = specie


    def breathe(self):
        result = super().breathe()
        return  f"{result}, это {self.specie} дышит легкими"


    def run(self):
        return f"{self.name}, {self.specie} бежит по саванне"



animal = Animal('Zver')
print(animal.breathe())

fish = Fish('Nemo', 'Fish-Cloun')
print(fish.breathe())
print(fish.swim())


lion = Lion('Simba', 'Lion')
print(lion.breathe())
print(lion.run())