def outer(par):
    loc = par

    def inner():
        return loc

    print(inner)
    return inner

var = 1
result = outer(var)
print(result())

