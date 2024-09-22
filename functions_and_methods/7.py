
# Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# This will raise an exception as too few arguments were provided for 
# number of parameters set.

# # SOLUTION
# The code will raise an error:
# ```
# TypeError: foo() missing 1 required positional
# argument: 'qux'
# ```
# We've defined foo with two parameters. However, we've only passed it 
# one argument. This is an error.