def run():
    # Create a dictionary whose:
    # - keys are of the first 100 natural numbers not divisible by 3
    # - values are those same numbers cubed
    my_dict = {}

    for i in range (1, 101):
        if i%3 != 0:
            my_dict[i] = i**3

    print("Classic method:")
    print(my_dict, "\n")

    # Do the same but using comprehension
    comp_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
    print("Comprehension method:")
    print(comp_dict)

if __name__ == '__main__':
    run()