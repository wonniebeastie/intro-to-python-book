# Use a `while` loop to print the numbers in `my_list`, one number per 
# line. Then, do the same with a `for` loop.

# GOAL
# Print numbers in given list using a `while` loop, then a `for` loop.

# INPUTS & OUTPUTS
# I: A list
# O: One number on each line

# EXAMPLE(S)
# I: [6, 3, 0, 11, 20, 4, 17]
# O:
# 6
# 3
# 0
# 11
# 20
# 4
# 17

# RULES (EXPLICIT/IMPLICIT)
# - One number per line
# - `while` loop must be used
# - `for` loop must be used
# - Number should be printed

# DS
# `while` loop
# `for` loop

# STEPS
# Given a list of numbers,

# Iterate through each number on list,
# print each one.

my_list = [6, 3, 0, 11, 20, 4, 17]

# `while` loop
index = 0

while index < len(my_list):
	print(my_list[index])
	index += 1

# `for` loop
for num in my_list:
	print(num)


# SOLUTION

# while_loop.py
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1

# for_loop.py
my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    print(number)


# Our solution using a `while` loop uses indexing to control iteration 
# and to access the list members. Note that we start by setting `index` 
# to `0` and then iterate while `index` is less than the list length.

# The solution using a `for` loop is clearly easier to understand -- we 
# don't have to mess around with indexing; we only need to iterate over 
# the list elements.