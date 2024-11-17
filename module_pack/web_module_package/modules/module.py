# файл модуля для того чтобы показать функционал if __name__ == '__main__'
__counter = 0


def sum_list(nums_list: list):
    '''Функция для сумирования элементов списка'''
    global __counter
    __counter += 1
    new_sum = 0
    for num in nums_list:
        new_sum += num
    return new_sum


def product_list(nums_list: list):
    global __counter
    __counter += 1
    product = 1
    for num in nums_list:
        product *= num
    return product


if __name__ == "__main__":
    print("Я предпочёл бы быть модулем! Но я могу провести для вас некоторые тесты")
    my_nums_list = [i for i in range(1, 6)]
    print(sum_list(my_nums_list))
    print(product_list(my_nums_list))
else:
    print("Я модуль! И мне это нравится!")