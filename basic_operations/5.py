# Will an error occur if you try to access a list element with an index
# greater than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# Yes this will result in an error because there is no corresponding
# value.

# SOLUTION
# Yes, an error will occur: list index out of range. When you use an 
# index value with no corresponding element, Python raises an `IndexError` 
# error.