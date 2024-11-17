
my_list_comprehension = [1 if num_c % 2 == 0 else 0 for num_c in range(10)]
my_generator = (1 if num_c % 2 == 0 else 0 for num_c in range(10))


print(my_list_comprehension)

for value in my_generator:
    print(value, end=' ')

print(len(my_list_comprehension))

