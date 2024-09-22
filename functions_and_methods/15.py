# Using the code below, classify the identifiers as global, local, or 
# built-in. For our purposes, you may assume this code is the entire 
# program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Line 1 - multiply (global)
# Line 1 - left, right (local)
# Line 8 - get_num (global)
# Line 8 - prompt (local)
# Line 9 - float (built-in)
# Line 9 - input (built-in)
# Line 11 - first_number (global)
# Line 11 - second_number (global)
# Line 13 - product (global)
# Line 14 - print (built-in)