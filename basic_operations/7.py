# What will the following code do? Why?

print(int('3.1415'))

# This will be explicitly coerced to the integer `3.1415`.

# SOLUTION
# This raises a `ValueError` since the string value `'3.1415'` does not 
# represent a valid integer. 