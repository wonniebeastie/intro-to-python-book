# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# This code outputs:
# ```
# Empty
# ```

# An empty list is passed to the function `is_list_empty()` on line 9.
# There's an `if` statement inside the function that will execute if
# `my_list` is truthy. 

# The body in this case will not execute because an empty list is a 
# falsy value. Other falsy values include `False`, `None`, all numeric
# zeros, empty strings, and other empty collections. Everything else 
# are truthy.

# So the program will go onto the `else` statement on the code on line
# 7 will execute.