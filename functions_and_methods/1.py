# What happens when you run the following program? Why do we get that 
# result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# It raises an `NameError` exception. 

# This is due to Python's scoping rules. # Variables defined inside 
# functions are local to that function, meaning that you can't acess
# them from outside it.

# Here, when we call the `print()` function on line 8 and attempt to
# access `foo`, it raises an exception because the `foo` can't be 
# reached from outside the `set_foo()` function.