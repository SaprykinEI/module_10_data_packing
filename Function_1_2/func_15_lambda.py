def printFunction(args, fun):
    for x in args:
        print(f'f({x}) = {fun(x)}', sep=',  ')


printFunction([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)