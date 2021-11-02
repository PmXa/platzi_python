from data import DATA

def run():
    # List comprehension to list all python devs and Platzi workers
    python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print("Python devs: ")
    for worker in python_devs:
        print(worker)
    print("-"*40)

    # List comprehension to list all Platzi workers
    platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("Platzi workers: ")
    for worker in platzi_workers:
        print(worker)
    print("-"*40)
    
    # HOF to filter all adults
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = map(lambda worker: worker["name"], adults)
    print("Adults: ")
    for worker in adults:
        print(worker)
    print("-"*40)

    # HOF to filter old people
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 69}, DATA))
    print("Old people: ")
    for worker in old_people:
        print(worker)
    print("-"*40)


if __name__ =='__main__':
    run()