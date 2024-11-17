my_dict = {'cat': 'Кошка', 'dog': 'Собака', 'Bird': 'Птица'}


my_dict_keys = my_dict.keys()
my_dict_values = my_dict.values()

print(my_dict)
print(my_dict_keys)
print(my_dict_values)
print(type(my_dict_values))
print(type(my_dict_keys))

print(list(my_dict_keys))
print(list(my_dict_values))

keys_list = [key for key in my_dict]
print(keys_list)

for key in my_dict:
    print(key)

