def run():

    # Dictionaries in lists
    pepes_nerd = [
        {"number": "1", "name":"Guty"},
        {"number": "2", "name":"Armando"},
        {"number": "3", "name":"Marco"},
        {"number": "4", "name":"Shake"},
        {"number": "5", "name":"Pol"},
        {"number": "6", "name":"Jorge"},
        {"number": "7", "name":"Bean"},
        {"number": "8", "name":"Edgar"},
        {"number": "9", "name":"Mooze"},
        {"number": "10", "name":"Filip"},
        {"number": "11", "name":"MMM"},
        {"number": "12", "name":"Brendita"},
        {"number": "13", "name":"Lisset"},
    ]

    # Lists in dictionaries
    number_families = {
        "natural": [0, 1, 2, 3, 4, 5],
        "integer": [-2, -1, 0 , 1, 2],
        "real": [-4.5, -2.53, 2.718, 3.14]
    }

    # The number super dictionary
    for key, value in number_families.items():
        print(key, " - ", value)

    # The Pepe's Nerd super list
    print("The Pepe's Nerd team:")
    for member in pepes_nerd:
        for key, value in member.items():
            print(key, value)


if __name__ == '__main__':
    run()