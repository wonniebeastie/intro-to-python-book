

def sum_of_squares(num1, num2):
    def square(num):
            return num * num

    return square(num1) + square(num2)

# Write a nested function in `sum_of_squares` that will make this code 
# work as shown.

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)


# SOLUTION
# Same as above.

# In this solution, we've added a nested function to calculate the 
# square of the number passed to it as an argument. Assuming we don't 
# need square anyplace else in our code, we can nest it inside 
# `sum_of_squares` to help keep the global scope "clean"; that is, 
# the global scope doesn't include anything that isn't used by the 
# top-level code.

