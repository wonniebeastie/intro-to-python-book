# Identify all of the function names and parameters present in the 
# code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Line 1 - multiply (function name), left & right (parameters)
# Line 7 - get_num (function name), prompt (parameter)
# Line 8 - float (function name), input (function name), prompt (parameter)
# Line 10 & 11 - get_num (function name)
# Line 12 - multiply (function name)
# Line 13 - print (function name)

# SOLUTION

# Function names:
# - multiply: defined on line 1, used on line 9.
# - get_num: defined on line 4, used on lines 7 and 8.
# - float: built-in function used on line 5.
# - input: built-in function used on line 5.
# - print: built-in function used on line 10.

# Parameters:
# - left and right are defined on line 1 and then used on line 2.
# - prompt is defined on line 4 and then used on line 5.

# `left` & `right` are referenced on line 2, but when they're inside the
# functions, they're spoken of as local variables instead of parameters.

# Likewise, `prompt` is defined as a parameter on line 4, but used as a
# local variable on line 5.