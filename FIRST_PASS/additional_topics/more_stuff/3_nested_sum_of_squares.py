# Consider the following code:

# def sum_of_squares(num1, num2):
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   
# print(sum_of_squares(5, 12))  

# Returns: NameError: name 'square' is not defined


# Write a nested function in sum_of_squares that will make this code work as shown.


def sum_of_squares(num1, num2):
    def square(number):
        return number * number
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

"""
The function called sum_of_squares takes two arguments.

It calls for another function called `square` but such a function is nowhere
to be found in the program.

So this was fixed by adding a nested funtion to first square each of the
numbers passed to the sum_of_squares/outer function.

Then when the result is returned, they are added together in the outer 
function.

It now works as intended.
"""