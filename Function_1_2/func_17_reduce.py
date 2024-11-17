#reduce(function, iterable, [initializer])

from functools import reduce

my_nums_list = [i + 1 for i in range(5)]
print(my_nums_list)
reduce_sum = reduce(lambda x, y: x + y, my_nums_list)
print(reduce_sum)


reduce_product = reduce(lambda x, y: x * y, my_nums_list)
print(reduce_product)