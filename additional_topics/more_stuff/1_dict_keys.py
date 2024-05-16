# What does the following function do? Be sure to identify the output value.

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

print(do_something(my_dict))  # CHRIS


"""
This function takes a single parameter, named `dictionary`. 

It calls the .keys() method on it, which creates a dictionary view object with
just the keys:

dict_keys(['Karl', 'Clare', 'Karis', 'Trevor', 'Antonina', 'Chris'])


Then the sorted() built-in function is called on these keys, returning:

['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']


It then calls the .upper() string method on the element with the index # 1,
which is "Chris", returning:

CHRIS

"""