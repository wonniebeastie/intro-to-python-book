dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# Without running this code, what will it print? Why?


# This will print `42`.

# Line 6 creates a shallow copy of `dict1` and assigns it to `dict2`.
# The dict constructor, when passed a dictionary as an argument, creates
# a shallow copy of that dictionary. 

# Shallow copies are duplicates of the original object except for the
# nested objects, which are shared between the copies and the original
# object.

# When the element at index 1 (`2`) of the value that corresponds to the key 
# `'a'` is reassigned with `42`on line 7, this change is reflected in
# the output of `dict2['a']`


# SOLUTION

# The code outputs:
# ```
# [1, 42, 3]
# ```

# As in the previous exercise, the constructor invocation `dict(dict1)` 
# creates a new dict that contains the same key/value pairs as `dict1`. 
# Thus, `dict2` is not the same object as `dict1`.

# On line 7, we reassign `dict1['a'][1]` to `42`. Since `dict1` and 
# `dict2` are different dicts, you might expect that mutating one of 
# `dict1`'s values would not impact `dict2`. However, that is not the 
# case. The dicts are different objects but share value components since 
# the dict constructor creates a shallow copy. Thus, mutations to 
# `dict1['a']` can be seen in `dict2['a']`.

# This code demonstrates that two dicts with equal-value objects 
# associated with every key may also share those objects. That isn't 
# always the case, but you must understand what's happening in your 
# code.


# NOTES
# - I should have read more carefully and saw that line 8 is to print
# the entire value that corresponds to the `'a'` key, not just the 
# reassigned value.

# - I should have pointed out that the changes were reflected in `dict2`
# as well because the value - the list `[1, 2, 3]` is a nested object,
# so is shared between the copy (`dict2`) and the original (`dict1`)

