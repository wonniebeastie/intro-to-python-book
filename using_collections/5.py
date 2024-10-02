# Which of the following values can't be used as a key in a `dict` 
# object, and why?

'cat' 
(3, 1, 4, 1, 5, 9, 2) 
['a', 'b'] # Lists are mutable, therefore, unhashable
{'a': 1, 'b': 2} # Dictionaries are mutable, therefore, unhashable
range(5)
{1, 4, 9, 16, 25} # Sets are mutable, therefore, unhashable
3
0.0
frozenset({1, 4, 9, 16, 25})

# SOLUTION
# Correct.

# The first value is a list, the second another dict, and the last a 
# set. Since all 3 types are mutable, they can't be used as dict keys. 
# All remaining items are immutable built-in objects; they are acceptable 
# dict keys.

# NOTE
# Sets are mutable but the members of a set must be immutable & hashable.