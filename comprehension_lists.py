def run():
    # First 100 squares
    squared = []

    for i in range(1, 101):
        squared.append(i**2)

    print("First 100 natural numbers squared:")
    print(squared)

    # First 100 squares of numbers NOT divisible by 3
    square_not_3 = []

    for i in range(1, 101):
        if (i%3 != 0):
            square_not_3.append(i**2)

    print("First 100 natural numbers but non-divisible by 3 numbers squared:")
    print(square_not_3,"\n")

    # List comprehension method
    print("For every <i> in from 1 to 100, append <i²> only if <i%3 != 0>")
    squares = [i**2 for i in range(1, 101) if (i%3 != 0 )]
    print(squares)

if __name__ == '__main__':
    run()