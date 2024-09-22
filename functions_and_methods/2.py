# Take a look at this code snippet:
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# This program prints:
# ```
# bar
# ```

# There are two variables called `foo` in this code:
# The `foo` in the global scope on line 2 & the `foo` in the local scope inside
# the `set_foo()` function on line 5. 

# When the `print()` function prints `foo` on line 8, it only has access to the 
# `foo` in the global scope, which is why it prints `'bar'`.