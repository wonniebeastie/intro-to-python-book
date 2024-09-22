# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# This will print:
# ```
# 42
# 3.141592
# 2.718
# ```

# Three parameters are set for the function `foo()`, with the last two 
# given default values. 

# When the function is invoked with 3 arguments, these explicitly 
# provided values override the default ones given to the last two.