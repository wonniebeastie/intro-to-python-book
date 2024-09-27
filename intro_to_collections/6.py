# Assuming you have the following assignment:

pi = 3.141592

# Write some code that converts the value of `pi` to a string and 
# assigns it to a variable named `str_pi`.

str_pi = str(pi)

print(str_pi) # 3.141592
print(repr(str_pi)) # '3.141592'

# SOLUTIONS

# 1
pi = 3.141592
str_pi = str(pi)

# Solution 1 is the preferred solution since it is slightly more 
# readable.

# 2
pi = 3.141592
str_pi = f'{pi}'
# Solution 2 works, too. However, f-strings are better suited for 
# creating strings mixed with other text.