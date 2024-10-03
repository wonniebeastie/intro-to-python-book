# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of `my_list`. In 
# this problem, you should write code that creates a new list with one 
# element for each number in `my_list`. If the original number is an 
# even, then the corresponding element in the new list should contain 
# the string `'even'`; otherwise, the element should contain `'odd'`.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# Expected Output:
# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]


# Given a list of numbers,

# Iterate through the list and create a new list:
# If original number is even, add "even" to the list,
# otherwise, add "odd" to the list.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for num in my_list:
	if num % 2 == 0:
		new_list.append('even')
	else:
		new_list.append('odd')

print(new_list)

# SOLUTION
# Correct.

# Our approach is straightforward: we iterate over all the numbers in 
# the list and check whether each is even. Based on the result, we 
# append either `'even'` or `'odd'` to the `result` list.

# May have struggled if you tried to use a list comprehension for this
# problem (which I tried to, lol). Since comprehensions don't have an 
# `else` capability, trying to generate `'even'` for some values and 
# `'odd'` for others is challenging.

# You can use a ternary expression in the comprehension, but this is a
# little confusing visually:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = [ 'even' if number % 2 == 0 else 'odd'
        for number in my_list ]
print(result)

# On line 7 (67 here) we've used a ternary expression to choose between
# the two values. The ternary is equivalent to:

if number % 2 == 0:
    return 'even'
else:
    return 'odd'

# A cleaner approach is to use a helper function to determine whether we
# should add `'even'` or `'odd'` to the new list:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
        for number in my_list ]
print(result)