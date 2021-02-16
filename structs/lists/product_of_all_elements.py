def product_of_all_elements(lst):
    left, right = 1, 1
    product = []

    for ele in lst:
        product.append(left)
        left = left * ele

    for i in range(len(product) - 1, -1, -1):
        print(product[i], '*', right)
        product[i] = right * product[i]
        right = right * lst[i]

        print(product)

    return product


def main():
    lst = [1, 2, 3, 4]
    product = product_of_all_elements(lst)
    print(product)


main()
