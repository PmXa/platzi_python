def run():
    my_list = [1, 9, 4, 5, 88, 94, 51, 61, 14, 3]

    # Filter only the odd numbers
    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)


if __name__ == "__main__":
    run()