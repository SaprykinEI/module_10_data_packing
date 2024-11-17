my_dict = {'cat': 'Кошка', 'dog': 'Собака'}
# print(my_dict['Bird'])

# word = 'bird'
#
# if word in my_dict:
#     print(my_dict[word])
# else:
#     print("Не знаю таких слов")


# word = 'cat'
# try:
#     print(my_dict[word])
# except KeyError:
#     print(f"Значения {word} нет в словаре")
# finally:
#     print(f"Программа завершила свою работу")


get_animal = my_dict.get('cat')
print(get_animal)
get_animal_1 = my_dict.get('bird')
print(get_animal_1)


get_animal_2 = my_dict.setdefault('dog')
print(get_animal_2)
print(my_dict)

get_animal_3 = my_dict.setdefault('bird')
print(my_dict)
print(get_animal_3)