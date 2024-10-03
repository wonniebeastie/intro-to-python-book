# GOAL
# To write a dictionary comprehension using a given set of strings as 
# the source.

# INPUTS & OUTPUTS
# I: given set (with strings as members)
# O: A dictionary 

# RULES (EXPLICIT/IMPLICIT)
# - Use the set given by `my_set` as the source of the strings.
# - Resulting dict object must have the strings as the keys whose values
# must be the length of the corresponding key.
# - Only keys with odd lengths should be in the dict.

# DS
# Sets
# Dictionary comprehension

# [ key_expression: value_expression for item in object if condition ]

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

pets_n_length = { name: len(name) for name in my_set if len(name) % 2 != 0 }

print(pets_n_length)
# {'Cocoa': 5, 'Cheddar': 7, 'Pudding': 7}

# SOLUTION
# The same as mine.

# Remember: sets are unordered, so your result may have a different 
# ordering.