def divisors(num):
    divisors = [i for i in range(1, num + 1) if num%i == 0]
    return divisors


def run():
    try:
        number = input("Enter a number: ")
        number = int(number)
        print(divisors(number))
    except ValueError:
        print("Must enter a number")


if __name__ == '__main__':
    run()