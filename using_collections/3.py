# GOAL
# Create new tuple from existing one.

# RULES (EXPLICIT/IMPLICIT)
# - Existing: `(1, 2, 3, 4, 5)`
# - Result should be: `(4, 3, 2)` - reversed & excluding the first & last

existing_tuple = (1, 2, 3, 4, 5)

print(existing_tuple[3:0:-1]) # (4, 3, 2)

# NOTES
# Slicing: positive indexes mean counting left-to-right, negative step
# value means sequence will be reversed.
# So started out by counting from 0, got to 3 (which is `4`) - which I
# included because starting values are INCLUSIVE. 
# Then put 0 as the stopping value, as we WANT the `2`, but putting 1
# here would give me `(4, 3)` as stopping values EXCLUSIVE. So 0 must
# be sepecified to exclude the `1` (index 0), not `2` (index 1).

# SOLUTIONS

# Several ways to solve this problem.

# 1
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)       # (4, 3, 2)

# First inclinication may have been to use the `.reverse()` method, but
# `.reverse()` only works with lists, so we have to first convert the 
# tuple to a list.
# We still have to slice the list, even though it's a little cleaner.


# 2 
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)


# 3
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)       # (4, 3, 2)

# Solutions 2 & 3 use the same approach by extracting a reversed slice.
# The only difference is in how we specify the start & stop values.
# Tricky element: the element indexed by the stop value is not included
# in the result.
# Using one of these solutions, you likely started with an off-by-one
# bug.
