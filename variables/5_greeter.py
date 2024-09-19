# Write a program named greeter.py that greets 'Victor' three times. 
# Your program should use a variable and not hard code the string value 
# 'Victor' in each greeting. Here's an example run of the program:

# $ python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

name = 'Ricky Bobby'

print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')

# SOLUTION

# This solution uses concatenation
name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# This solution uses f-string interpolation
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')

# First, we create a variable that holds the value 'Victor'. 
# With a variable, we don't need to hard code 'Victor' each time we 
# greet him. Instead, we can use the variable as part of an expression. 
# In our first solution, we use string concatenation; in the second, 
# we use f-string interpolation.