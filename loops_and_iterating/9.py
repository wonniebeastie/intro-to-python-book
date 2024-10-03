# GOAL
# To write a function that computes & returns the factorial of a number.

# INPUTS & OUTPUTS
# I: a positive integer
# O: an integer (factorial of input)

# EXAMPLE(S)
# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000

# RULES (EXPLICIT/IMPLICIT)
# - Argument is always a positive integer (`n`).
# - Must be done using a `for` or `while` loop.
# - All numbers from `1` to `n` must be multiplied & result returned.

# QUESTIONS?
# What is a factorial?
# A factorial of a positive integer is defined as the product of all
# integers between `1` and `n`, inclusive:
# n!	Expansion	Result
# 1!	1	1
# 2!	1 * 2	2
# 3!	1 * 2 * 3	6
# 4!	1 * 2 * 3 * 4	24
# 5!	1 * 2 * 3 * 4 * 5	120

# DS
# Range object
# `for` loop / `while` loop




def factorial(n):
	range_of_nums = list(range(1, n + 1))
	# print(range_of_nums)
	product = 1

	for num in range_of_nums:
		product *= num
	
	return product


print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000


# SOLUTION

# while loop
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

# for loop
def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

# Our first solution uses a `while` loop to compute the return value. We 
# begin by assigning the result variable to 1, then we multiply result 
# by all of the integers between `n` and `1`, inclusive. Note that we need 
# to decrement `n` by `1` at the end of each iteration.

# The second solution is similar, but it uses a `for` loop instead of a 
# `while` loop. The benefit of using for is that we don't need to worry 
# about decrementing n. Instead, we just iterate over the integers 
# between `n` and `1`, inclusive, using a range.