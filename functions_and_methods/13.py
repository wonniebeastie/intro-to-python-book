# Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This will raise an exception. When you give a parameter a default
# value, you must also give the parameters following that one a 
# default value. 

# SOLUTION
# The code will raise an error:
# ```
# SyntaxError: non-default argument follows default argument
# ```

# Here, we've defined foo with three parameters, with the second 
# parameter having a default value. This is an error, however. 
# Once Python sees a positional parameter with a default value, 
# all subsequent parameters must have default values.


# NOTES
# Was confused whether the exception will be raised due to `third` not
# being provided a default value as well, OR if it would be due to `third`
# not being provided an explicit value.
# But it looks like it was the former - I'm guessing because the function 
# definition comes before the function invocation.