# Modify the `age.py` program you wrote in Exercise 3 of the Input/Output
# chapter. The updated code should use a `for` loop to display the future 
# ages.

# Exercise 3
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {int(age) + 10} years old.')
# print(f'In 20 years, you will be {int(age) + 20} years old.')
# print(f'In 30 years, you will be {int(age) + 30} years old.')
# print(f'In 40 years, you will be {int(age) + 40} years old.')

# GOAL
# Rewrite `age.py` to use a `for` loop instead.

# INPUTS & OUTPUTS
# I: user input as an integer
# O: In 10 year... etc.

# RULES (EXPLICIT/IMPLICIT)
# - `for` loop must be used
# - The output message should be repeated 4 times.
# - Year should start out at 10.
# - Age should start out at `age` + 10.
# - Both year & age should be incremented by 10 each time.

# DS
#

# STEPS
# Set `age` variable with user input, as an integer.

# Display "You are `age` years old."

# `year` is 0

# A loop is created that will loop 4 times.
# Increment `year` by 10 each loop.
# Increment `age` by 10 each loop.
# 'In `year` years, you will be `age` + 10 years old.

age = int(input("How old are you?: "))

year = 0

for decade in range(4):
	year += 10
	print(f'In {year} years, you will be {age + year} years old.')


# SOLUTION

# age = int(input('How old are you? '))
# print(f'You are {age} years old.')
# print()

# for future in range(10, 50, 10):
#     print(f'In {future} years, you will be '
#         f'{age + future} years old.')