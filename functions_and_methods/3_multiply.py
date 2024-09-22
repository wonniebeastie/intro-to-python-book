# Write a program that uses a multiply function to multiply two 
# numbers and returns the result. Ask the user to enter the two 
# numbers, then output the numbers and result as a simple equation.

# Goal
# Writing a function that multiplies 2 #s and returns result.

# Inputs & Outputs
# I: 2 numbers
# O: result

# Example
# I: 3.1416, 2.7183
# O: 8.53981128

# Rules (explicit/implicit)
# - The two numbers must be user-provided
# - Display the questions & equation 
# - Numbers in floats
# - Numbers should be outputted as a simple equation

def multiply(num1, num2):
	return num1 * num2

first_num = float(input("Enter the first number: ")) # Repetition
second_num = float(input("Enter the second number: ")) # Repetition

product = multiply(first_num, second_num)

print(f"{first_num} * {second_num} = {product}")


# NOTES
# Remember to write functions to do only one thing.
# Define functions at the top.
# Forgot the implicit rule for float at first.
# Remember that the `input()` function returns strings, not integers or
# floats.
# You can test the function before writing the rest of the code to make
# sure it's working well.

# SOLUTION
def multiply(left, right):
    return left * right

def get_number(prompt): # Function to avoid repetition
    entry = input(prompt) 
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')