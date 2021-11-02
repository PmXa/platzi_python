def run():
    # Given a list, return the list's elements squared
    my_list = [1, 2, 3, 4, 5]
    
    # For method
    for_list = []
    
    for element in my_list:
        for_list.append(element**2)
    
    print("Loop method: ")
    print(for_list, "\n")
    
    # Comprehension method
    comp_list = [i**2 for i in range(1,6)]
    print("List comprehension method:")
    print(comp_list, "\n")

    # HOF method:
    map_list = list(map(lambda x: x**2, my_list))
    print("Using map(): ")
    print(map_list)


if __name__ == '__main__':
    run()