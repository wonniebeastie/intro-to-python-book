dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line


# This program is nearly identical to that of the previous exercise. 
# However, this time, it should create a shallow copy of `dict1`. Be 
# careful: you're not allowed to use the `copy` module in this exercise.`

# In addition, before you run this code, can you predict the output values?


# MY SOLUTION
print(dict1         is dict2)         # False
print(dict1['a']    is dict2['a'])    # True, because the value is a nested list.
print(dict1['a'][0] is dict2['a'][0]) # True, nested set.
print(dict1['a'][1] is dict2['a'][1]) # True, nested list.
print(dict1['b']    is dict2['b'])    # True, nested tuple.
print(dict1['b'][0] is dict2['b'][0]) # True, nested set.
print(dict1['b'][1] is dict2['b'][1]) # True, nested list.

# NOTE TO SELF
# `dict2 = dict1[:]` does not work because slicing is supported by
# indexing. Dictionaries do not support access by numeric index - only
# by keys.


# SOLUTION
# Same as mine.

# Since the constructors for Python's built-in collections all return 
# a shallow copy, we used the `dict` constructor to create a shallow 
# copy of `dict1`.

# The first `print` statement prints `False` since `dict1` and `dict2` 
# are different objects. However, the nested components are all 
# references to the original nested objects. Thus, the remaining print 
# statements print `True`.