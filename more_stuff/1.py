def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# What does this function do? Be sure to identify the output value.

# step 1
# `dictionary.keys()` returns: dict_keys(['Karl', 'Clare', 'Karis', 'Trevor', 'Antonina', 'Chris'])

# step 2
# The sorted function returnes: ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']

# step 3
# `[1]` targets element at index 1, which is `'Chris'`, and the `upper()` method is called on it,
# returning `'CHRIS'`

# step 4
# The function outputs: CHRIS


# MY SOLUTION
# This function creates a list of just the key names from the dictionary
# passed as the argument, sorts the list in ascending order, then takes
# the element at index 1 of the list and returns it in all upper case 
# letters.

# The output value is:
# ```
# CHRIS
# ```