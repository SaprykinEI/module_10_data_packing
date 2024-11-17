# animals_tuple_1 = ('Cat', 'Turtle', 'Snake', 'Dog',)
# print(len(animals_tuple_1))
#
# nums_tuple = (1, 2, 3, 4, 5.5,)
# print(nums_tuple)
#
# print(min(animals_tuple_1))
# print(min(nums_tuple))
# print(max(nums_tuple))
# print(max(animals_tuple_1))


animals_tuple_1 = ('Cat', 'Turtle', 'Snake', 'Dog',)
nums_tuple = (1, 2, 3, 4, 5.5,)

sorted_tuple_animals = tuple(sorted(animals_tuple_1, reverse=True))
print(sorted_tuple_animals)

sorted_tuple_nums = tuple(sorted(nums_tuple, reverse=True))
print(sorted_tuple_nums)