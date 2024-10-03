# Print all of the even numbers in the following list of nested lists. 
# Don't use any `while` loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

# Expected output:
# 6
# 4
# 2
# 4
# 16
# 0

for list_of_nums in my_list:
	for num in list_of_nums:
		if num % 2 == 0:
			print(num)

# SOLUTION
# Correct

# That may not have been too easy. Nested loops are hard to think 
# about, but you'll encounter them often enough to have dreams about 
# them. We start by iterating over the nested lists inside `my_list`. 
# That means `nested_list` takes on the values `[1, 3, 6, 11]`, 
# `[4, 2, 4]`, and `[9, 7, 16, 0]` as the iteration proceeds. 

# We then iterate over the numbers in the current nested list 
# during each iteration. Finally, we print the even numbers.