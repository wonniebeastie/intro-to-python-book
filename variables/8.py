# Challenge: This program uses a bit of math. Don't let that scare you 
# away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to 
# find a bank that pays you 5% (this is a wish-fulfillment fantasy) 
# compounded interest every year. After one year, you will have $1,050 
# ($1,000 times 1.05). 

# After two years, you will have $1,050 times 1.05, or $1102.50. 

# Create a variable named `balance`` that contains the amount 
# of money you will have after 5 years, then print the result. 

# Use a single expression if you can to set `balance` to the correct value.

# PEDAC
# I: float - 1000.00
# O: float - 1050.00 (after one year)

# I: 1050.00
# O: 1102.50 (after 2 years)

# Rules
# - Start: 1000_00
# - Bank pays you 5% compounded interest every year (money x 1.05)
# - Create variable `balance` - contains money after 5 years
# - Print result
# - Use a single expression to set `balance` to correct value.

# Questions
# - What does `compounded` mean here?

# Algorithm
# SET balance = 1000.00
# SET interest = 1.05
# 
# WHILE loop hasn't looped 5 times yet:
#     balance = old balance x interest
#     READ balance
#
# PRINT balance after 5 years

balance = 1000.00
interest = 1.05

for _ in range(5):
	balance = balance * interest
	print(f'Balance: ${balance:.2f}')

# SOLUTION
balance = (1000.00 * 1.05 * 1.05 * 1.05
                   * 1.05 * 1.05)
print(balance)

#The program prints `1276.2815625000003` as the final balance. That's 
# not precisely correct. The actual value should be `1276.2815625`. 
# That's close enough when you consider the imprecision of using floats.