def run():
    # Create a list with all numbers less than 5 digits long that are multiples of 4, 6 and 9
    overly_complicated_list = [i for i in range(1, 99999) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]
    print(overly_complicated_list)


if __name__ == '__main__':
    run()