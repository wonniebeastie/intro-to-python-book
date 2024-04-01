my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)


def find_integers(collection):
    return [ element for element in collection if type(element) is int ]
    # for element in collection:
    #     number = type(element) is int
    #     if number == True:
    #         print(element) 


integers = find_integers(my_tuple)


print(integers)                    # [1, 3, -4]