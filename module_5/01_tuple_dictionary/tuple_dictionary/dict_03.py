my_dict = {'cat': 'Кошка', 'dog': 'Собака'}
print(my_dict['cat'])

my_dict['die Katze'] = my_dict['cat']
print(my_dict)

del my_dict['cat']
print(my_dict)

# popped_data = my_dict.pop('dog')
# print(popped_data)
my_dict['der Hund'] = my_dict.pop('dog')
print(my_dict)