# How would you print all the numbers in the following range?
range(3, 17, 4)

# You must use a constructor to explicitly coerce the range object into
# something else to access the elements.

print(set(range(3, 17, 4)))    # {11, 3, 15, 7}
print(list(range(3, 17, 4)))   # [3, 7, 11, 15]
print(tuple(range(3, 17, 4)))  # (3, 7, 11, 15)


# SOLUTION

# 1
print(list(range(3, 17, 4)))

# 2
print(tuple(range(3, 17, 4)))

# Since ranges are lazy sequences, you must either iterate over the
# range or convert the range to a non-lazy sequence: a list or tuple.
# Here, we transform the range into a list and a tuple.