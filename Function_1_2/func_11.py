my_list = []

for num in range(10):
    my_list.append(1 if num % 2 == 0 else 0)

print(my_list)


my_list_comprehension = [1 if num_c % 2 == 0 else 0 for num_c in range(10)]
print(my_list_comprehension)
