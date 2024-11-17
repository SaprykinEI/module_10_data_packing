# my_fruit = ('Яблоко', 'Яблоко-Груша', 'Ананас', 'Слива', 'Яблоко')
#
# fruit = input("Введите фрукт: ")
# print(my_fruit.count(fruit))
#
#
#
tuple_fruit = ('Яблоко', 'ЯблокоГруша', 'Ананас', 'Слива', 'Яблоко')
fruit_inp = input("Введите фрукт: ")
count = 0
for fruit in tuple_fruit:
    if fruit_inp in fruit:
        count += 1
print(count)


# tuple_auto = ('BMW', 'Audi', 'Mercedes', 'BMW', 'Audi', 'Toyota', 'Lada', 'BMW')
#
# car_name = input("Введите название производителя который нужно заменить: ")
# new_car_name = input("Введите на что заменить: ")
#
# car_list = list(tuple_auto)
#
# for car in range(len(tuple_auto)):
#     if car_list[car] == car_name:
#         car_list[car] = new_car_name
#
# print(car_list)
#
# tuple_auto = tuple(car_list)
# print(type(tuple_auto))
# print(tuple_auto)
