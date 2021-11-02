def run():
    # Create a dictionary whose
    # - keys are the first 1000 natural numbers
    # - values are the square roots of those numbers

    overly_complicated_dict = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(overly_complicated_dict)


if __name__ == '__main__':
    run()