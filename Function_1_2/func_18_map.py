my_list = [x for x in range(6)]
print(my_list)
my_list_2 = list(map(lambda x: 2 ** x, my_list))
print(my_list_2)


my_gen = (x for x in range(5))

my_gen_2 = list(map(lambda x: 2 ** x, my_gen))
print(my_gen_2)

l = [i for i in range(5)]
print(l)

b = (z for z in range(5))
for value in b:
    print(value)


v = [s for s in range(10)]
print(v)
zov = lambda y: 3 + y
k = list(map(zov, v))
print(k)
for n in k:
    print(n)