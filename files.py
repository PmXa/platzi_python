# Function definitions
def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)


def write():
    bands = [
        "The Offspring",
        "The V-Town Have-Nots",
        "Rise Against",
        "Kaotiko",
        "Segismundo Toxicómano"
    ]
    with open("./files/bands.txt", "w", encoding="utf-8") as file:
        for name in bands:
            file.write(name)
            file.write("\n")


def a_write():
    bands = [
        "Desakato",
        "No Konforme",
        "Whisky Caravan",
        "Envidia Kotxina",
        "Juan Gabriel"
    ]
    with open("./files/bands.txt", "a", encoding="utf-8") as file:
        for name in bands:
            file.write(name)
            file.write("\n")


# Main function & entry point
def run():
    read()
    write()
    a_write()


if __name__ == '__main__':
    run()