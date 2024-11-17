my_list_one = []

for exp in range(6):
    my_list_one.append(10 ** exp)

my_list_two = [10 ** exp for exp in range(6)]

print(my_list_one)
print(my_list_two)
