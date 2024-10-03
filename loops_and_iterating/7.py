# Write a `find_integers` function that returns a list of all the 
# integers from `my_tuple`:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)

# integers = find_integers(my_tuple)

# print(integers)                    # [1, 3, -4]

# You can use the expression `type(object) is int` to determine whether 
# an object is an integer. For instance:

print(type(True) is int)      # False (boolean)
print(type([1, 2, 3]) is int) # False (list)
print(type(3.141592) is int)  # False (float)
print(type(77) is int)        # True

# You may receive a SyntaxWarning warning message from the last two 
# examples. You can ignore that warning.


# MY SOLUTION

# Steps
# Create an empty list.

# Given a list of objects -

# Iterate through the list
# Check if each item is an integer.
# If it is an integer, add it to the list.
# Otherwise, go onto the next item.

# Regular `for` loop solution:
def find_integers(list_of_stuff):
	new_list = []
	for item in list_of_stuff:
		if type(item) is int:
			new_list.append(item)
		else:
			continue
	
	return new_list

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)

print(integers)  # [1, 3, -4]


# list comprehension solution:
# [ expression for item in object if condition ]
def find_integers(list_of_stuff):
	return [ item for item in list_of_stuff if type(item) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)

print(integers)                    # [1, 3, -4]


# SOLUTION
def find_integers(things):
    return [ element
            for element in things
            if type(element) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

# Our solution uses a list comprehension to iterate through the elements
# in `things` argument and create a new list.

# It's worth nothing that we used a list comprehension to iterate over
# the tuple. The main reason for that choice is that `find_integers` is
# expected to return a list, not a tuple.

# However, an even more important reason is that there is no such thing
# as a "tuple comprehension".

# Comprehensions don't care what kind of collection you're iterating,
# but the result must always be a list, set, or dictionary.

