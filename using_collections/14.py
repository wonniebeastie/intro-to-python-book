# Assume you have the following sequences:
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. Print the 
# final result so you can see all the values, which should look like 
# this:

# [('a', 'Alpha', None, 10),
#  ('b', 'Bravo', True, 20),
#  ('c', 'Charlie', False, 30)]

# print(list(zip(my_str, my_list, my_tuple, my_range)))
# [('a', 'Alpha', None, 10), ('b', 'Bravo', True, 20), ('c', 'Charlie', False, 30)]

# SOLUTION
result = zip(my_str, my_list, my_tuple, my_range)
print(list(result))

# NOTES
# The returning value by the `zip` function is lazy.
# So to get the elements to be printed, you have to use a loop to iterate
# over it or use a iterable constructor.

print(tuple(result)) # ()
# Most lazy sequences are "used up" once you access it once, unlike the 
# `range` object.