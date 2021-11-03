def divisors(num):
# Use assert statements to stop the user from entering a negative number
    assert num > 0, "Negative numbers and <0> are not supported!"
    divisors = [i for i in range(1, num + 1) if num%i == 0]
    return divisors

def run():
    number = input("Enter a number: ")
    assert number.isnumeric(), "Must enter a number!"
    print(divisors(int(number)))


if __name__ == '__main__':
    run()