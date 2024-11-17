my_fruit = ('Яблоко', 'Яблоко-Груша', 'Ананас', 'Слива', 'Яблоко')

fruit = input("Введите фрукт: ")
print(my_fruit.count(fruit))



my_fruit_1 = ('Яблоко', 'Яблоко-Груша', 'Ананас', 'Слива', 'Яблоко')
fruit_1 = input("Введите фрукт: ")
count = 0
for fruit_1 in my_fruit:
    if fruit_1 in my_fruit:
        count += count

print(count)