def greet_deeply_curried(greeting):
    def w_separator(separator):
        def w_emhasis(emhasis):
            def w_name(name):
                print(greeting + separator + name + emhasis)

            return w_name

        return w_emhasis

    return w_separator


greet = greet_deeply_curried("Привет")("|")("!")
greet("Evgeniy")
greet("Ivan")


greet_deeply_curried_lambda = lambda greeting: lambda separator: lambda emhasis: lambda name: print(greeting + separator + name + emhasis)
greet_lambda = greet_deeply_curried_lambda("Доброго времени суток")("../..")("?")
greet_lambda("Дмитрий")