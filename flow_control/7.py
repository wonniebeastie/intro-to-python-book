# GOAL
# Write a function that takes 1 integer & print a message that describes
# whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

# INPUTS & OUTPUTS
# I: single integer
# O: {single integer} is between/greater than/less than {number range}

# EXAMPLE(S)
# I: 0
# O: 0 is between 0 and 50

# I: 25
# O: 25 is between 0 and 50

# I: 50
# O: 50 is between 0 and 50

# I: 75
# O: 75 is between 51 and 100

# I: 100
# O: 100 is between 51 and 100

# I: 101
# O: 101 is greater than 100

# I: -1
# O: -1 is less than 0

# RULES (EXPLICIT/IMPLICIT)
# - Function name should be `number_range()` as per example.
# - Single integer param
# - Number must be identified to be:
#   - Less than or equal to -1   ["is less than 0"]
#   - 0 ~ 50 (inclusive)         ["between 0 and 50"]
#   - 51 ~ 100 (inclusive)       ["between 51 and 100"]
#   - Greater than 101           ["is greater than 100"]
# So between 4 statements/choices

# DS
# if-else
# or match-case

# STEPS
# Define function `number_range(int)`
#     If `int` < 0, print "{int} is less than 0"
#     If `int` >= 0 and `int` <= 50, print "{int} is between 0 and 50"
#     If `int` >= 51 and `int` <= 100, print "{int} is between 51 and 100"
#     If `int` > 100, print "{int} is greater than 100"

def number_range(int):
	if int > 100:
		print(f'{int} is greater than 100')
	elif int >= 0 and int <= 50:
		print(f'{int} is between 0 and 50')
	elif int >= 51 and int <= 100:
		print(f'{int} is between 51 and 100')
	else:
		print(f'{int} is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0

# SOLUTION
def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

# NOTES
# Less confusing to go from a high number to 0 to 50, then 51 to 100,
# then to lower than 0, so go from order, ascending or descending.

# It's more readable to do only one condition for each one - the lower
# range will be caught by the previous condition anyways.

# We can use string concatenation, but you would have to convert the 
# integer to string to print it, so that's extra work; So string 
# interpolation works better here.