from data import DATA

def print_list(my_list):
    for element in my_list:
        print(element)
    print("-"*40)

def run():
    # Create the python_devs list using filter() and map()
    python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    python_devs = list(map(lambda worker: worker["name"], python_devs))
    print("Python devs:")
    print_list(python_devs)

    # Create the platzi_workers list using filter() and map()
    platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    platzi_workers = list(map(lambda worker: worker["name"], platzi_workers))
    print("Platzi workers: ")
    print_list(platzi_workers)
    
    # Create the adults list using list comprehension
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    print("Adults: ")
    print_list(adults)

    # Create the old_people list using list comprehension
    old_people = [worker["name"] for worker in DATA if worker["age"] >= 70]
    print("Old people: ")
    print_list(old_people)


if __name__ == '__main__':
    run()