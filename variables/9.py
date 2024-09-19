# Repeat the previous question but, this time, use augmented assignment 
# to compute the final result, one year at a time.

# balance = (1000.00 * 1.05 * 1.05 * 1.05
#                    * 1.05 * 1.05)
# print(balance)

balance = 1000.00

balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(balance)

# SOLUTION
# The same as mine
# This program also prints 1276.2815625000003 as the final balance. Once 
# again, that's close enough.