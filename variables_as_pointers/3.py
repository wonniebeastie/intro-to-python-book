dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# Without running this code, what will it print? Why?

# This code will print:
# ```
# The Life of Brian
# ```

# When `dict2` is initialized on line 7 with `dict1` passed as an
# argument to the dictionary constructor, what is assigned to `dict2`
# is the shallow copy of the dictionary assigned to `dict1`. 

# Shallow copies are duplicates of the original object except for the 
# nested objects; Meaning that they are new, independent objects from 
# the original they were copied from. 

# So reassigning the value to the `'Monty Python'` key in `dict2` on line 8 
# does not reflect on `dict1` on line 9, which is why it prints 'The 
# Life of Brian'.


# SOLUTION

# The code outputs:
# The Life of Brian

# The constructor call `dict(dict1)` creates a new dict that contains 
# the same key/value pairs as `dict1`. Thus, `dict2` is not the same 
# object as `dict1`. When we change the value associated with the 
# `'Monty Python'` key in `dict2`, we don't see a corresponding change 
# in `dict1`.

# This code demonstrates that two identical objects aren't necessarily 
# the same object. If you assign an object associated with variable `a` 
# to variable `b`, the variables share that object. However, if the 
# value assigned to `b` is an entirely new object, there is no sharing, 
# even if the values are identical.

