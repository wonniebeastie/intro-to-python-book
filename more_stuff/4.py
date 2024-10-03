def increment_counter():
	global counter
	counter += 1

counter = 0 

# Write a function called `increment_counter` that increments a `counter` 
# variable every time it is called. You can test your code with the 
# following:

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101


# SOLUTION

counter = 0

def increment_counter():
    global counter
    counter += 1

# In this solution, we've first initialized a global `counter` variable
# to `0`. Our `increment_counter` function simply increments this
# variable each time the function is called.

# However, since we're using `counter += 1` in the code, we need to tell
# Python that `counter`, as used in `increment_counter`, is a global 
# cariable. 

# We do this by including `global counter` in the function definition.