# What will the following code print?
print('abc-def'.isalpha()) # False
print('abc_def'.isalpha()) # False
print('abc def'.isalpha()) # False
print('abc def'.isalpha() and
    'abc def'.isspace()) # False
print('abc def'.isalpha() or
    'abc def'.isspace()) # False
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False
print('31_415'.isdigit()) # False
print('3.1415'.isdigit()) # False
print(''.isspace()) # False

# SOLUTION
# Correct

# Two things to note:

# Lines 4-7:
# You can't use `and` or `or` to determine whether a string contains 
# a mixture of different value types. The `str.isXXXXX` methods determine 
# whether every character in strmatches a certain class of characters. 
# Thus, a string can't be both alphabetic and whitespace. It can be 
# alphabetic or whitespace, but that doesn't work for something like 
# `'abc def'`.

# Line 13
# Most of the `str.isXXXXX` methods return `False` when invoked by an 
# empty string.
