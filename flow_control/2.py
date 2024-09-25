# GOAL
# To write a function that determines whether its argument is an odd
# even number.

# INPUTS & OUTPUTS
# I: A number
# O: 'even' or 'odd'

# RULES (EXPLICIT/IMPLICIT)
# - Function name should be `even_or_odd`
# - If argument is even, print `'even'`
# - Otherwise, print `'odd'`
# - Assume argument is always an integer

# STEPS
# Set function `even_or_odd(number)`
# 	If `number` is divisible by 2, print `'even'`.
#   Otherwise, print `'odd'` 

def even_or_odd(num):
	if num % 2 == 0:
		print('even')
	else:
		print('odd')

even_or_odd(34823989) # odd
even_or_odd(0) # even
even_or_odd(-82) # even


# SOLUTION
# 1
def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

# 2
def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')

# The solutions use the modulo operator (%) to determine whether the 
# number is even. If the result of number % 2 is 0, the number is even.

# The second solution shows the equivalent solution using a ternary 
# expression. The author isn't sure whether this is more readable than 
# the first solution.