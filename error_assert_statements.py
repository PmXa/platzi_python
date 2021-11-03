def divisors(num):
    try: 
        if num < 1:
            raise ValueError("Can't accept <0> or negative numbers")

        divisors = [i for i in range(1, num + 1) if num%i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    number = input("Enter a number: ")
    assert number.isnumeric(), "Must enter a number!"
    print(divisors(int(number)))


if __name__ == '__main__':
    run()