pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Without running the following code, what values will be printed by 
# line 10? Why?

# Line 10 will print:
# ```
# dict_keys(['Cat', 'Bird', 'Snake'])
# ```

# The `keys` variable is initialized on line 7 with the value returned
# by the `keys` dictionary method. At this point in the program, the
# value would be a special list tied to the `pets` dictionary that
# includes just the keys from the dictionary: `['Cat', 'Dog', 'Bird']`.

# However, the key `'Dog'` is removed from the `pets` dictionary on line
# 8, then a new key-value pair (`'Snake': 'Sssss'`) is added to it on
# line 9.

# These changes are reflected in the view object assigned to `keys`, as
# dictionary view objects are dynamic & offer a window view into 
# the current state of the dictionary they were called on.

# SOLUTION
# dict_keys(['Cat', 'Bird', 'Snake'])
# Since `dict.keys` returns a dictionary view object, any changes made 
# to the dictionary after you call the `keys` method will be reflected 
# in dictionary view referenced by `keys` immediately.

