def greet(greeting, name):
    print(f"{greeting}, {name}")


greet("Привет", "Евгений")


def greet_curried(greeting):
    def greet(name):
        print(f"{greeting}, {name}")

    return greet

greet_hello = greet_curried("Привет")
print(greet_hello)
greet_hello("Иван")