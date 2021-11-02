from functools import reduce

def run():
    my_list = [1, 2, 3, 4, 5, 6]

    product = reduce(lambda a,b: a*b, my_list)
    print(product)


if __name__ == '__main__':
    run()