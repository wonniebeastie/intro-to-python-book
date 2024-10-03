set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))

print(set2)

# Without running this code, what will it print? Why?

# Don't worry about having an exact match for the output. The important
# part is to show something that accurately represents `set2`.


# MY SOLUTION

# This will print something like:
# ```
# {42, 'Monty Python', range(5, 10), ('a', 'b', 'c')}
# ```

# This is because the reference to the set that is assigned to `set1` 
# on  line 1 is assigned to `set2` on line 2, creating an alias of 
# `set1`.

# And since both variables point to the same object in memory, mutating
# the set assigned to `set1` with the `add()` method on line 3 can also 
# be seen when printing `set2`.


# SOLUTION

# The code outputs:

# The order of the elements probably won't match,
# but the 4 elements shown here should all be
# present in your answer.

{('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}

# This result demonstrates that `set1` and `set2` reference the same 
# set: if we add an element to set1, we'll see that element when we 
# look at `set2`. The opposite is true, too: if we add something to 
# `set2`, we'll see it in set1.

# This code also demonstrates that assigning a variable to another 
# variable doesn't create a new object. Instead, Python copies a 
# reference from the original variable (`set1`) into the target variable
# (`set2`).