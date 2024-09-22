# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# It will print:
# ```
# 42
# 3.141592
# 2
# ```

# The first argument passed to the `foo()` function will be printed as 
# normal, then the second argument will override the default value of `3`.

# The third output, `2`, is the default value given to the parameter `third`.
# Default values can be given to parameters as "fallback" values allowing the
# function to be called without arguments for these.
