def divisors(num):
    # Intentional logic error: mnum & i == 0
    divisors = [i for i in range(1, num + 1) if num%i == 1]
    return divisors


def run():
    number = input("Enter a number: ")
    number = int(number)

    print(divisors(number))


if __name__ == '__main__':
    run()