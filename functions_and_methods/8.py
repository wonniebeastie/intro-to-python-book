# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# This code will raise an exception:
# ```
# TypeError: foo() takes 2 positional arguments but 3 were given
# ```

# Providing too many arguments than what the parameters are set for
# results in an error.

# In this code, only 2 parameters were set by the function but 3 
# arguments were passed to the function.


# SOLUTION
# The code will raise an error:
# ```
# TypeError: foo() takes 2 positional arguments,
# but 3 were given
# ```
# We've defined foo with two parameters. However, we've passed the 
# function three arguments. This is an error.


# NOTES
# Don't forget to say number of parameters & arguments.