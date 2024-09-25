# Write a function called increment_counter that increments a counter 
# variable every time it is called. You can test your code with the following:

counter = 0 

def increment_counter():
    global counter   # Tells Python "I want to change the global variable counter"
    counter += 1 


print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

"""
Solution: Initialize a global variable called `counter`. 

The function `increment_counter` simply increments this variable each time
it is called by using augmented assignment of += 1. 

The `global` keyword is used to tell the function that the `counter` variable
it is modifying should be the `counter` variable in the global scope. 

Without the `global` keyword, Python assumes that that the variable is local 
to the function's scope.
"""