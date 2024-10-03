# Challenging Problem: 
# Don't feel bad if you struggle with this problem or can't solve it. 
# The problem is not easy. It is designed to demonstrate why we prefer 
# to use for loops when we can, and a big part of that problem is messy 
# code that is difficult to write and understand. See how far you can 
# get, but don't spend much time struggling.

# Print all of the even numbers in the following list of nested lists. 
# This time, don't use any `for` loops.

# PEDAC

# GOAL
# To print all the even numbers in the following list of nested lists.

# INPUTS & OUTPUTS
# I: a list with nested lists (all integers inside)
# O: an even number from those lists on each line

# EXAMPLE(S)
# I: [[1, 3, 6, 11], [4, 2, 4], [9, 17, 16, 0]]
# O:
# 6
# 4
# 2
# 4
# 16
# 0

# RULES (EXPLICIT/IMPLICIT)
# - Cannot use a `for` loop
# - Only even numbers must be printed

# QUESTIONS?

# DS
# `while` loop

# STEPS
# variable `index` = 0

# keep looping while `index` < length of `my_list`:
# 	`nested_index` = 0
# 	keep looping while `nested_index` < length of each element in `my_list`
#   	if element at `nested_index` % 2 == 0, 
#       	print(element)

my_list = [
	[1, 3, 6, 11],
	[4, 2, 4],
	[9, 17, 16, 0],
]

index = 0

while index < len(my_list):
	nested_index = 0

	while nested_index < len(my_list[index]):
		if my_list[index][nested_index] % 2 == 0:
			print(my_list[index][nested_index])
		nested_index += 1
	index += 1



# SOLUTION

my_list = [
	[1, 3, 6, 11],
	[4, 2, 4],
	[9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1

# Phew! That's messy and hard to follow, isn't it? While the individual 
# loops aren't tough to understand, keeping track of two different 
# indexes and getting them to work together is no mean feat. We also 
# have to use both indexes on lines 10 and 11.

# We can simplify this solution a bit by assigning each nested list to 
# a local variable:
my_list = [
	[1, 3, 6, 11],
	[4, 2, 4],
	[9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_list = my_list[outer_index]
    inner_index = 0
    while inner_index < len(inner_list):
        number = inner_list[inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1