from sys import path


path.append((r'Z:\Training\Top-school\Class Work\module_pack\web_module_package\modules'))


from modules.module import sum_list, product_list

if __name__ == "__main__":
    zeroes = [0 for i in range(5)]
    ones = [1 for j in range(5)]
    print(sum_list(zeroes))
    print(product_list(ones))

