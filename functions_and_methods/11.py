# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# This will print:
# ```
# 42
# 3
# 2
# ```

# The provided value, `42`, will be passed to the function `foo()`
# as an arugment for the parameter `first`, then the default values for
# the parameterse `second` and `third` will be printed.

# Default parameters allow functions to be called without specifying 
# arguments.