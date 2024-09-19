# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# This code prints:
# ```
# Good Morning, Victor
# Good Afternoon, Victor
# Good Evening, Victor
# Good Morning, Nina
# Good Afternoon, Nina
# Good Evening, Nina
# ```
# This happens because the variable `NAME` is reassigned the value `'Nina'`
# on line 8. Even though it was initialized first with the value `'Victor'`,
# and the variable is in all uppercase letters signifying a constant, it can 
# be reassigned just like a regular variable because Python does not have a 
# built-in way to make constants.


# SOLUTION
# The program first greets Victor 3 times. It then greets Nina 3 times.

# Unfortunately, Python doesn't have real constants. There's no way to 
# prevent the reassignment of NAME. If this faux-constant really needs 
# to be changed, you should use a regular variable instead:

name = 'Victor'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)

name = 'Nina'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)