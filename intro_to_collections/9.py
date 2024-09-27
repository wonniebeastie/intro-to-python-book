my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your
# answers:

# 1. Are the lists assigned to `my_list` and `another_list` equal?

# Yes, they are equal in value, as `[1, 2, 3, [4, 5, 6]]` is assigned
# to both of them.
print(another_list) # [1, 2, 3, [4, 5, 6]]

# 2. Are the lists assigned to `my_list` and `another_list` the same object?

# No, they are not the same object. When `my_list` is passed as an 
# argument to the list constructor, a shallow copy of it is created.
# The shallow copy is a new object, independent of the original object
# it was copied from.
print(id(my_list))      # 4300311872
print(id(another_list)) # 4300237760

# 3. Are the nested lists at index 3 of `my_list` and `another_list` equal?

# Yes, they are equal in value.
print(my_list[3])      # [4, 5, 6]
print(another_list[3]) # [4, 5, 6]

# 4. Are the nested lists at index 3 of `my_list` and `another_list` the same object?

# Yes the nested lists in both are the same object. Both lists hold a
# reference to where the nested list is stored in memory & share the
# object between them. 

# SOLUTION

# 1. The two lists are equal: they are both lists with the same elements.

# 2. The two lists are not the same object: The list constructor creates 
# a new object.

# 3. The two nested lists are equal: they are both lists that have the 
# same elements.

# 4. The two nested lists are the same object: the list constructor 
# creates a shallow copy of the iterable passed as an argument. Shallow 
# copies don't create new nested lists. Instead, only a reference to 
# the nested list gets copied.